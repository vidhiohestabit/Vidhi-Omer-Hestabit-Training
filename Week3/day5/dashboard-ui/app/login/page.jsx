import Input from "../../components/ui/Input";

export default function LoginPage() {
  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 px-4">
      <div className="w-full max-w-sm bg-white rounded-xl shadow-md p-8">
        <form className="space-y-6">

          {/* Username */}
          <div className="relative">
            <span className="absolute inset-y-0 left-3 flex items-center text-gray-400">
              👤
            </span>
            <input
              type="text"
              placeholder="Username"
              className="w-full pl-10 pr-4 py-3 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-green-400"
            />
          </div>

          {/* Password */}
          <div className="relative">
            <span className="absolute inset-y-0 left-3 flex items-center text-gray-400">
              🔒
            </span>
            <Input
              type="password"
              placeholder="Password"
              className="w-full pl-10 pr-4 py-3 border rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-green-400!"
            />
          </div>

          {/* Remember + Forgot */}
          <div className="flex items-center justify-between text-sm text-gray-500">
            <label className="flex items-center gap-2">
              <input type="checkbox" className="rounded border-gray-300" />
              Remember me
            </label>
            <span className="hover:text-green-500 cursor-pointer">
              Forgot Password?
            </span>
          </div>

          {/* Button */}
          <button
            type="button"
            className="w-full bg-green-400 hover:bg-green-500 text-white py-3 rounded-lg font-semibold transition"
          >
            LOGIN
          </button>

        </form>
      </div>
    </div>
  );
}
