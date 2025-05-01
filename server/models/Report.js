import mongoose from "mongoose";

const reportSchema = new mongoose.Schema(
  {
    supervisorId: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
      required: true,
    },
    period: {
      type: String,
      required: true,
    },
    employeeIds: [
      {
        type: mongoose.Schema.Types.ObjectId,
        ref: "User",
      },
    ],
    summary: {
      type: Object,
      required: true,
    },
  },
  { timestamps: true }
);

export default mongoose.model("Report", reportSchema);
