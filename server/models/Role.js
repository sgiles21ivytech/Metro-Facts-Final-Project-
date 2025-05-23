import mongoose from "mongoose";

const roleSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: true,
      unique: true,
      trim: true,
    },
    permissions: [String],
  },
  { timestamps: true }
);

export default mongoose.model("Role", roleSchema);
