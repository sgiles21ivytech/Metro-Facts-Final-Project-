import Report from "../models/Report.js";
import PerformanceMetric from "../models/PerformanceMetric.js";

export const getReports = async (req, res, next) => {
  try {
    const reports = await Report.find({ supervisorId: req.user._id });
    res.json(reports);
  } catch (err) {
    next(err);
  }
};

export const createReport = async (req, res, next) => {
  try {
    const { period, employeeIds } = req.body;
    const metrics = await PerformanceMetric.find({
      userId: { $in: employeeIds },
      period,
    });

    const summary = metrics.reduce((acc, m) => {
      acc[m.userId] = acc[m.userId] || {
        tasksCompleted: 0,
        salesAmount: 0,
        salesTarget: 0,
      };
      acc[m.userId].tasksCompleted += m.tasksCompleted || 0;
      acc[m.userId].salesAmount += m.salesAmount || 0;
      acc[m.userId].salesTarget += m.salesTarget || 0;
      return acc;
    }, {});

    const report = new Report({
      supervisorId: req.user._id,
      period,
      employeeIds,
      summary,
    });
    await report.save();
    res.status(201).json(report);
  } catch (err) {
    next(err);
  }
};

export const getReportById = async (req, res, next) => {
  try {
    const report = await Report.findById(req.params.id);
    if (!report) return res.status(404).json({ message: "Report not found" });
    res.json(report);
  } catch (err) {
    next(err);
  }
};
