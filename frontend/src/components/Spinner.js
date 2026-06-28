import React from "react";
import "./Spinner.css";

export default function Spinner({ message, subtext }) {
  return (
    <div className="spinner-container" role="status" aria-live="polite">
      <div className="spinner-loader"></div>
      {message && <h4 className="spinner-title">{message}</h4>}
      {subtext && <p className="spinner-subtitle">{subtext}</p>}
    </div>
  );
}