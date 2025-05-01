import PerformanceMetric from "../models/PerformanceMetric.js";

export const getMetrics = async (req, res, next) => {
  try {
    const metrics = await PerformanceMetric.find({ userId: req.user._id });
    res.json(metrics);
  } catch (err) {
    next(err);
  }
};

export const createOrUpdateMetric = async (req, res, next) => {
  try {
    const { period, ...data } = req.body;
    const metric = await PerformanceMetric.findOneAndUpdate(
      { userId: req.user._id, period },
      { $set: data },
      { new: true, upsert: true }
    );
    res.status(201).json(metric);
  } catch (err) {
    next(err);
  }
};
