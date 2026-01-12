import mongoose from "mongoose";

const JobSchema = new mongoose.Schema({
  title: String,
  description: String,
  skills: [String]
});

export default mongoose.model("Job", JobSchema);
