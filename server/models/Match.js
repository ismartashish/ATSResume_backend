import mongoose from "mongoose";

const MatchSchema = new mongoose.Schema({
  resumeId: mongoose.Schema.Types.ObjectId,
  jobId: mongoose.Schema.Types.ObjectId,
  score: Number
});

export default mongoose.model("Match", MatchSchema);
