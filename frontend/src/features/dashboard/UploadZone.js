import React, { useState } from "react";
import { clientApiService } from "../../services/api";
import "./UploadZone.css";

export default function UploadZone({ onAnalysisSuccess, onAnalysisStart }) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [error, setError] = useState("");
  const [isProcessing, setIsProcessing] = useState(false);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    setError("");
    if (file && file.type === "application/pdf") {
      setSelectedFile(file);
    } else {
      setError("Please select a valid PDF file.");
      setSelectedFile(null);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!selectedFile) return;

    setError("");
    setIsProcessing(true);
    onAnalysisStart();

    try {
      const response = await clientApiService.uploadTranscript(selectedFile);
      onAnalysisSuccess(response.data);
    } catch (err) {
      setError("Failed to upload document. Please try again.");
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <div className="upload-card">
      <div className="card-header">
        <h3>Upload Transcript</h3>
        <p>Upload a PDF document to begin analysis.</p>
      </div>

      <form onSubmit={handleSubmit} className="form-wrapper">
        <label className="drop-zone">
          <input type="file" hidden accept=".pdf" onChange={handleFileChange} />
          <p>{selectedFile ? selectedFile.name : "Click to select a PDF"}</p>
        </label>

        {error && <div className="error-banner">{error}</div>}

        <button type="submit" className="btn-submit" disabled={!selectedFile || isProcessing}>
          {isProcessing ? "Processing..." : "Analyze Document"}
        </button>
      </form>
    </div>
  );
}