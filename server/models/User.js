import mongoose from "mongoose";

const userSchema = new mongoose.Schema(
  {
    email: {
      type: String,
      required: true,
      unique: true,
      trim: true,
      lowercase: true,
    },
    password: {
      type: String,
      required: true,
    },
    role: {
      type: String,
      enum: [
        "Customer Service",
        "Customer Service Supervisor",
        "Sales",
        "Sales Supervisor",
        "Software Developer",
        "Software Developer Supervisor",
      ],
      required: true,
    },
  },
  { timestamps: true }
);

const User = mongoose.model("User", userSchema);
export default User;
