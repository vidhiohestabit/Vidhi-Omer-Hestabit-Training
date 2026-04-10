export default function Profile() {
  return (
    <div className="max-w-4xl mx-auto space-y-6">

      {/* Cover */}
      <div className="h-40 rounded-xl bg-gradient-to-r from-green-400 to-teal-500 relative" />

      {/* Profile Card */}
      <div className="bg-white p-6 rounded-xl shadow-md -mt-16">
        
        {/* Top Section */}
        <div className="flex flex-col md:flex-row items-center md:items-end gap-6 mb-6">
          <img
            src="/profile.jpeg"
            alt="Profile"
            className="w-28 h-28 rounded-full border-4 border-white object-cover"
          />

          <div className="text-center md:text-left flex-1">
            <h2 className="text-2xl font-bold">Nina Valentine</h2>
            <p className="text-gray-500">Actress • Public Figure</p>
            <p className="text-sm text-gray-400">nina_val@example.com</p>
          </div>

          <button className="px-4 py-2 bg-teal-500 text-white rounded-lg text-sm">
            Edit Profile
          </button>
        </div>

        {/* Stats */}
        <div className="grid grid-cols-3 gap-4 text-center border-y py-4 mb-6">
          <div>
            <h3 className="text-lg font-semibold">128</h3>
            <p className="text-xs text-gray-500">Posts</p>
          </div>
          <div>
            <h3 className="text-lg font-semibold">12.4K</h3>
            <p className="text-xs text-gray-500">Followers</p>
          </div>
          <div>
            <h3 className="text-lg font-semibold">86</h3>
            <p className="text-xs text-gray-500">Projects</p>
          </div>
        </div>

        {/* Info Grid */}
        <div className="grid md:grid-cols-2 gap-6 mb-6">

          {/* Social Links */}
          <div className="space-y-3">
            <h3 className="text-gray-500 font-semibold">Social Profiles</h3>
            <a href="https://linkedin.com" className="block text-teal-500">
              🔗 linkedin.com
            </a>
            <a href="https://x.com" className="block text-teal-500">
              🐦 x.com
            </a>
            <a href="https://facebook.com" className="block text-teal-500">
              📘 facebook.com
            </a>
          </div>

          {/* Details */}
          <div className="space-y-3">
            <h3 className="text-gray-500 font-semibold">Details</h3>
            <p className="text-sm text-gray-600">Location: Los Angeles, USA</p>
            <p className="text-sm text-gray-600">Joined: March 2023</p>
            <p className="text-sm text-gray-600">Role: Admin</p>
          </div>
        </div>

        {/* Bio */}
        <div>
          <h3 className="text-gray-500 font-semibold mb-2">About</h3>
          <p className="text-gray-700 text-sm leading-relaxed">
            Nina Valentine is a professional actress with over 10 years of experience
            in film and television. Passionate about storytelling, creative direction,
            and community engagement. Actively working on multiple international projects
            and collaborations.
          </p>
        </div>

      </div>
    </div>
  );
}
