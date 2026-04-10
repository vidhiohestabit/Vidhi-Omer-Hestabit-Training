const getUsers = (req, res) => {
  res.json([{ id: 1, name: "Vidhi" }, { id: 2, name: "Omer" }]);
};

module.exports = { getUsers };