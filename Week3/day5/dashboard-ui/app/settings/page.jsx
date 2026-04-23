import Card from "../../components/ui/Card";
import Button from "../../components/ui/Button";

export default function SettingsPage() {
  return (
    <div className="space-y-8">

      {/* Header */}
      <div>
        <h1 className="text-2xl font-semibold">Settings</h1>
        <p className="text-sm text-gray-500">
          Manage your account and application preferences
        </p>
      </div>

      {/* General Settings */}
      <Card>
        <h3 className="text-lg font-semibold mb-1">General Settings</h3>
        <p className="text-sm text-gray-500 mb-6">
          Control how the application behaves
        </p>

        <div className="space-y-5">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium">Email Notifications</p>
              <p className="text-xs text-gray-500">
                Receive updates and alerts via email
              </p>
            </div>
            <Button variant="secondary" className="hover:bg-amber-900">
              Enabled
            </Button>
          </div>

          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium">Dark Mode</p>
              <p className="text-xs text-gray-500">
                Reduce eye strain in low-light environments
              </p>
            </div>
            <Button variant="secondary">Disabled</Button>
          </div>

          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium">Auto Updates</p>
              <p className="text-xs text-gray-500">
                Keep the app up-to-date automatically
              </p>
            </div>
            <Button variant="secondary">Enabled</Button>
          </div>
        </div>
      </Card>

      {/* Account Settings */}
      <Card>
        <h3 className="text-lg font-semibold mb-1">Account Settings</h3>
        <p className="text-sm text-gray-500 mb-6">
          Manage your personal information
        </p>

        <div className="space-y-5">
          <div className="flex items-center justify-between">
            <span className="text-sm">Change Password</span>
            <Button variant="secondary">Update</Button>
          </div>

          <div className="flex items-center justify-between">
            <span className="text-sm">Two-Factor Authentication</span>
            <Button variant="secondary">Enable</Button>
          </div>

          <div className="flex items-center justify-between">
            <span className="text-sm">Connected Devices</span>
            <Button variant="secondary">View</Button>
          </div>
        </div>
      </Card>

      {/* Danger Zone */}
      <Card>
        <h3 className="text-lg font-semibold text-red-500 mb-1">
          Danger Zone
        </h3>
        <p className="text-sm text-gray-500 mb-6">
          Irreversible account actions
        </p>

        <div className="flex items-center justify-between">
          <p className="text-sm text-gray-600">
            Delete your account permanently
          </p>
          <Button className="bg-red-500 hover:bg-red-600">
            Delete Account
          </Button>
        </div>
      </Card>

      {/* Save */}
      <div className="flex justify-end">
        <Button>Save Changes</Button>
      </div>

    </div>
  );
}
