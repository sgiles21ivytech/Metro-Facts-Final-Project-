import mongoose from "mongoose";

const performanceMetricSchema = new mongoose.Schema(
  {
    userId: {
      type: mongoose.Schema.Types.ObjectId,
      ref: "User",
      required: true,
    },
    period: {
      type: String,
      required: true, // Format like '2024-04'
    },
    tasksCompleted: Number,
    customerSatisfaction: Number,
    salesAmount: Number,
    salesTarget: Number,
  },
  { timestamps: true }
);

export default mongoose.model("PerformanceMetric", performanceMetricSchema);
