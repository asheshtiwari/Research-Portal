/**
 * API Service layer for backend communication.
 * Automatically switches between Local and Production environments.
 */

// Key: REACT_APP_BACKEND_URL
// Value: https://research-portal-36cs.onrender.com

const API_BASE_URL = process.env.REACT_APP_BACKEND_URL || "http://127.0.0.1:8000";

export const clientApiService = {
  uploadTranscript: async (file) => {
    const formData = new FormData();
    formData.append("file", file);

    try {
      // Yahan humne base URL ko dynamic rakha hai
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
      console.error("API Error details:", error);
      throw error;
    }
  }
};