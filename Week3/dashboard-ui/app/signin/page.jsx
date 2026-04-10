import Card from "../../components/ui/Card";
import Input from "../../components/ui/Input";
import Button from "../../components/ui/Button";

export default function SignInPage() {
  return (
    <div className="max-w-md mx-auto mt-16 space-y-6">
      <Card>
        <h2 className="text-xl font-semibold mb-2">Sign In</h2>
        <p className="text-sm text-gray-500 mb-6">
          Enter your credentials to access your account
        </p>

        <div className="space-y-4">
          <Input placeholder="Email address" />
          <Input placeholder="Password" type="password" />
        </div>

        <div className="mt-6">
          <Button className="w-full bg-amber-300 hover:bg-amber-900">
            Sign In
          </Button>
        </div>
      </Card>
    </div>
  );
}
