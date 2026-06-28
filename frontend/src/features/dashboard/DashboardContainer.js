import React, { useState } from "react";
import UploadZone from "./UploadZone";
import ReportViewer from "./ReportViewer";
import Spinner from "../../components/Spinner";
import "./DashboardContainer.css"; 

export default function DashboardContainer({ currentActiveTab }) {
  const [analysisReport, setAnalysisReport] = useState(null);
  const [status, setStatus] = useState("idle"); 
  

  const [vaultRecords, setVaultRecords] = useState([
    { 
      name: "TCS_Q4_Transcript.pdf", 
      format: "PDF", 
      status: "Processed", 
      date: new Date().toLocaleDateString() 
    }
  ]);

  const resetWorkflow = () => {
    setAnalysisReport(null);
    setStatus("idle");
  };

  if (currentActiveTab === "analysis_engine") {
    return (
      <div className="dashboard-container">
        {status === "idle" && (
          <UploadZone 
            onAnalysisStart={() => setStatus("processing")}
            onAnalysisSuccess={(data) => {
              setAnalysisReport(data);
              setStatus("success");
            }}
          />
        )}

        {status === "processing" && (
          <Spinner message="Analyzing Document" subtext="Processing transcript metrics..." />
        )}

        {status === "success" && analysisReport && (
          <div>
            <div className="action-row">
              <button onClick={resetWorkflow} className="btn-secondary">
                Analyze Another
              </button>
            </div>
            <ReportViewer reportData={analysisReport} />
          </div>
        )}
      </div>
    );
  }

  // History tab  UI
  if (currentActiveTab === "document_vault") {
    return (
      <div className="vault-card">
        <div className="vault-header">
          <div>
            <h3>Document Vault</h3>
            <p>Historical analysis archive.</p>
          </div>
          {vaultRecords.length > 0 && (
            <button onClick={() => setVaultRecords([])} className="btn-danger">
              Clear History
            </button>
          )}
        </div>

        <div className="table-wrapper">
          {vaultRecords.length > 0 ? (
            <table className="data-table">
              <thead>
                <tr>
                  <th>Name</th>
                  <th>Date</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {vaultRecords.map((record, index) => (
                  <tr key={index}>
                    <td>{record.name}</td>
                    <td>{record.date}</td>
                    <td>{record.status}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          ) : (
            <p>No archival data found.</p>
          )}
        </div>
      </div>
    );
  }

  return null;
}