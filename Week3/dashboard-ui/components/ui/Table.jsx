export default function Table({ users }) {
  return (
    <div className="overflow-x-auto bg-white rounded shadow">
      <table className="min-w-full divide-y divide-gray-200">
        <thead className="bg-gray-50">
          <tr>
            <th className="px-6 py-3 text-left text-gray-500">Name</th>
            <th className="px-6 py-3 text-left text-gray-500">Role</th>
            <th className="px-6 py-3 text-left text-gray-500">Status</th>
            <th className="px-6 py-3 text-left text-gray-500">Employed</th>
          </tr>
        </thead>
        <tbody className="divide-y divide-gray-200">
          {users.map((user, idx) => (
            <tr key={idx} className="hover:bg-gray-50">
              <td className="px-6 py-4">{user.name}<br/><span className="text-gray-400 text-sm">{user.email}</span></td>
              <td className="px-6 py-4">{user.role}</td>
              <td className={`px-6 py-4 font-semibold ${user.status === "Online" ? "text-green-500" : "text-gray-400"}`}>{user.status}</td>
              <td className="px-6 py-4">{user.employed}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
