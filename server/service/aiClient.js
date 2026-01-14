// server/services/aiClient.js
import axios from "axios";

export const aiClient = axios.create({
  baseURL: "https://atsresume-ai.onrender.com",
});
