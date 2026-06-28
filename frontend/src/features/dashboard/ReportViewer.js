import React from "react";
import "./ReportViewer.css";

export default function ReportViewer({ reportData }) {
  if (!reportData) return null;

  const getBadgeClass = (value) => {
    const val = value.toLowerCase();
    if (val.includes("optimistic") || val.includes("high")) return "badge-green";
    if (val.includes("cautious") || val.includes("medium")) return "badge-yellow";
    if (val.includes("pessimistic") || val.includes("low")) return "badge-red";
    return "badge-default";
  };

  return (
    <div className="viewer-container">
      <div className="header-block">
        <h2 className="main-title">Equity Research Analysis Report</h2>
      </div>

      <div className="meta-grid">
        <div className="meta-card">
          <span>Management Tone</span>
          <span className={`badge ${getBadgeClass(reportData.management_tone)}`}>{reportData.management_tone}</span>
        </div>
        <div className="meta-card">
          <span>Confidence Level</span>
          <span className={`badge ${getBadgeClass(reportData.confidence_level)}`}>{reportData.confidence_level}</span>
        </div>
      </div>

      <div className="split-grid">
        <div className="panel-card">
          <h4>Strategic Positives</h4>
          <ul>
            {reportData.key_positives.map((item, i) => <li key={i}>{item}</li>)}
          </ul>
        </div>
        <div className="panel-card">
          <h4>Critical Challenges</h4>
          <ul>
            {reportData.key_challenges.map((item, i) => <li key={i}>{item}</li>)}
          </ul>
        </div>
      </div>

      <div className="full-width-card">
        <h4>Forward Guidance</h4>
        <p>{reportData.forward_guidance}</p>
      </div>
    </div>
  );
}