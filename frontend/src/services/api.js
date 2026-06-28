/**
 * API Service layer for backend communication.
 */

const API_BASE_URL = process.env.REACT_APP_BACKEND_URL || "http://127.0.0.1:8000";

export const clientApiService = {
  /**
   * Uploads a file to the backend for analysis.
   * @param {File} file - The PDF file object.
   */
  uploadTranscript: async (file) => {
    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch(`${API_BASE_URL}/api/v1/analysis/upload`, {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        const errorData = await response.json().catch(() => ({}));
        throw new Error(errorData.detail || "Server failed to process the request.");
      }

      return await response.json();
    } catch (error) {
      console.error("API Error:", error);
      throw error;
    }
  }
};