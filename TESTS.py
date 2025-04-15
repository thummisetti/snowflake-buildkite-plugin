import unittest
import subprocess

class TestSnowflakeBuildkitePlugin(unittest.TestCase):
    
    def test_sql_execution(self):
        """Test if a SQL query runs successfully in Snowflake."""
        command = ["buildkite-agent", "run", "SELECT 1;"]
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)
        self.assertIn("1", result.stdout)
    
    def test_missing_credentials(self):
        """Ensure missing credentials result in an appropriate error."""
        command = ["buildkite-agent", "run", "SELECT 1;"]
        env = {"SNOWFLAKE_USER": "", "SNOWFLAKE_PASSWORD": ""}
        result = subprocess.run(command, capture_output=True, text=True, env=env)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("authentication failed", result.stderr.lower())
    
    def test_invalid_query(self):
        """Ensure invalid SQL queries fail as expected."""
        command = ["buildkite-agent", "run", "SELECT INVALID_COLUMN FROM nonexistent_table;"]
        result = subprocess.run(command, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("error", result.stderr.lower())

if __name__ == "__main__":
    unittest.main()
