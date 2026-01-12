import axios from "axios";
import { ENV } from "../config/env.js";

export const callAI = (payload) =>
  axios.post(`${ENV.AI_URL}/analyze`, payload);
