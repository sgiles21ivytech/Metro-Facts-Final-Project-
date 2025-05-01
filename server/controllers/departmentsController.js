import Department from "../models/Department.js";

export const getDepartments = async (req, res, next) => {
  try {
    const departments = await Department.find();
    res.json(departments);
  } catch (err) {
    next(err);
  }
};

export const createDepartment = async (req, res, next) => {
  try {
    const { name } = req.body;
    const department = new Department({ name });
    await department.save();
    res.status(201).json(department);
  } catch (err) {
    next(err);
  }
};
