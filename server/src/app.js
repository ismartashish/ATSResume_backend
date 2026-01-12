import express from "express";
import cors from "cors";

import resumeRoutes from "./routes/resume.routes.js";
import jobRoutes from "./routes/job.routes.js";
import matchRoutes from "./routes/match.routes.js";
import templateRoutes from "./routes/template.routes.js";

const app = express();

app.use(cors());
app.use(express.json());

app.use("/api/resume", resumeRoutes);
app.use("/api/jobs", jobRoutes);
app.use("/api/match", matchRoutes);
app.use("/api/templates", templateRoutes);

app.get("/health", (_, res) => {
  res.json({ status: "OK" });
});

export default app;
