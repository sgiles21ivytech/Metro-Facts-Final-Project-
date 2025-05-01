import Role from "../models/Role.js";

export const getRoles = async (req, res, next) => {
  try {
    const roles = await Role.find();
    res.json(roles);
  } catch (err) {
    next(err);
  }
};

export const createRole = async (req, res, next) => {
  try {
    const { name, permissions } = req.body;
    const role = new Role({ name, permissions });
    await role.save();
    res.status(201).json(role);
  } catch (err) {
    next(err);
  }
};
