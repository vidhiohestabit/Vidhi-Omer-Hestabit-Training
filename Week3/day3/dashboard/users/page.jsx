const users = [
  { id: 1, name: "John Doe", email: "john@mail.com", role: "Admin" },
  { id: 2, name: "Jane Smith", email: "jane@mail.com", role: "User" },
];

export default function UsersPage() {
  return (
    <div className="p-6 space-y-6">
      
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-semibold text-gray-800">Users</h1>
          <p className="text-sm text-gray-500">
            Manage registered users
          </p>
        </div>

        <span className="text-sm bg-green-100 text-green-600 px-3 py-1 rounded-full">
          {users.length} Users
        </span>
      </div>

      {/* Table */}
      <div className="overflow-x-auto bg-white rounded-xl shadow-sm border">
        <table className="min-w-full text-sm">
          
          <thead className="bg-gray-50 text-gray-600 uppercase text-xs">
            <tr>
              <th className="px-6 py-4 text-left">User</th>
              <th className="px-6 py-4 text-left">Email</th>
              <th className="px-6 py-4 text-left">Role</th>
            </tr>
          </thead>

          <tbody>
            {users.map((user) => (
              <tr
                key={user.id}
                className="border-t hover:bg-gray-50 transition"
              >
                {/* User Info */}
                <td className="px-6 py-4 flex items-center gap-3">
                  <div className="w-9 h-9 rounded-full bg-green-100 text-green-600 flex items-center justify-center font-semibold">
                    {user.name.charAt(0)}
                  </div>
                  <span className="font-medium text-gray-800">
                    {user.name}
                  </span>
                </td>

                {/* Email */}
                <td className="px-6 py-4 text-gray-500">
                  {user.email}
                </td>

                {/* Role */}
                <td className="px-6 py-4">
                  <span
                    className={`px-3 py-1 rounded-full text-xs font-medium
                      ${
                        user.role === "Admin"
                          ? "bg-purple-100 text-purple-600"
                          : "bg-blue-100 text-blue-600"
                      }`}
                  >
                    {user.role}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>

        </table>
      </div>

    </div>
  );
}
