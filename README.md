# ContentGenerator
GUI based content generator given the specific keyword using OPEN AI GPT API.

Instructions on how to set up environment variable

To set an environment variable in PowerShell, use the `$env:` prefix. Here's the updated command:

```shell
$env:OPENAI_API_KEY='YOUR_API_KEY'
```

Replace `'YOUR_API_KEY'` with your actual OpenAI API key.

After running this command in the PowerShell terminal, your environment variable should be set for the current session. You can then run your Python code in VS Code, and it will be able to access the `OPENAI_API_KEY` environment variable.

Please note that if you close the PowerShell session or open a new one, you'll need to set the environment variable again. If you'd like to set the environment variable permanently on Windows, you can follow these steps:

1. Open the Start menu and search for "Environment Variables" and select "Edit the system environment variables".

2. In the System Properties window, click the "Environment Variables" button.

3. In the "User variables" section, click the "New" button.

4. Enter `OPENAI_API_KEY` as the variable name and your API key as the variable value.

5. Click "OK" to save the environment variable.

6. Close any existing terminals or restart your computer for the changes to take effect.

After completing these steps, the `OPENAI_API_KEY` environment variable will be available permanently on your Windows system, and your Python code in VS Code will be able to access it.
