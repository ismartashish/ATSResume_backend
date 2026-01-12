import mongoose from "mongoose";

const ResumeSchema = new mongoose.Schema({
  userId: mongoose.Schema.Types.ObjectId,
  skills: [String],
  score: Number
});

export default mongoose.model("Resume", ResumeSchema);
