import React, { useState } from "react";
import DashboardContainer from "./features/dashboard/DashboardContainer";
import "./App.css";
import './index.css';

export default function App() {
  const [activeTab, setActiveTab] = useState("analysis_engine");

  return (
    <div className="app-wrapper">
      <aside className="sidebar">
        <div style={{ padding: "24px" }}>
          <h2>Research Portal</h2>
        </div>
        
        <nav style={{ padding: "0 16px" }}>
          <div 
            onClick={() => setActiveTab("analysis_engine")}
            className={`nav-item ${activeTab === "analysis_engine" ? "active" : ""}`}
          >
            Analysis Engine
          </div>
          <div 
            onClick={() => setActiveTab("document_vault")}
            className={`nav-item ${activeTab === "document_vault" ? "active" : ""}`}
          >
            Document Vault
          </div>
        </nav>
      </aside>

      <div className="main-area">
        <header className="app-header">
          <small>System Date: {new Date().toLocaleDateString()}</small>
        </header>
        <main className="content-container">
          <DashboardContainer currentActiveTab={activeTab} />
        </main>
      </div>
    </div>
  );
}