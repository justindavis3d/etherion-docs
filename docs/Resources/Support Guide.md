# Support Guide
Our Discord server is an active community hub, and is our main method of resolving issues with customers.  
There you'll gain access to dedicated support channels where you can receive assistance from our team and other users.

- **Support hours:** 08:00–14:00 AEST (UTC+10:00)
- **Unavailable:** Weekends & Australian public holidays

[**Open Discord Server**](http://dsc.gg/etheriondesigns)

---

## **Before You Ask**

To help us assist you efficiently and effectively, please follow these guidelines before submitting a support request. This will often resolve your issue faster, or provide us with the crucial information needed for a quick diagnosis.  

1. **Ensure your support request meet our requirements**
    - You must be a verified customer who owns one or more of our assets
    - Your support request must related to our products:
        1. Regarding an issue you are having with it.
        2. Needing help in how to use it in a way that is stated or implied in the product description. _(We do not provide general unreal engine tutorship for newbies, or provide support to customers wishing to modify or extend the product outside of it's original intended use.)_
2. **Before applying for a Support ticket:**
    - Restart Unreal engine and check that the issue is consistent.
    - Check that **[[index|our documentation]]** doesn’t already answer your question.
    - Use Search Engines & A.I tools to try to answer your question first.  
        Some examples might include:  
        - [**Google**](https://google.com/)  
        - **[Perplexity](https://www.perplexity.ai/)**  
        - [**ChatGPT**](https://chat.openai.com/)  
        - [**Gemini**](https://gemini.google.com/app)  
        - **[Claude](https://claude.ai/new)**  
        - **[Deepseek](https:https://www.deepseek.com/en)**  
        
3. **Provide Detailed Information**A clear and detailed description of your issue is paramount. Instead of general statements like "My foliage isn't moving," provide specific details:
    - **Asset Name:** (example: Etherion Foliage Plugin Lite)
    - **Unreal Engine Version:** (e.g., UE5.3.2, UE5.4.1)
    - **Operating System (OS):** (Please mention if not using Windows 11)
    - **Context:** Is the issue occurring in the Unreal Editor (PIE), Standalone Game, or a packaged build?
    - **Replication Steps:** A clear, step-by-step guide on how we can reproduce the issue.
    - **Relevant Blueprint Screenshots or Videos:** If the issue involves your Blueprint implementation, screenshots of the relevant nodes are required.
    - **Logs:** Attach the appropriate logs from your project's /Saved/Logs/ directory (see "Where to Find Your Logs" below).
    - **Any Recent Changes:** Did the issue appear after a specific change you made (e.g., engine upgrade, new plugin, specific Blueprint modification)?  
        
4. **Include relevant Screenshots, Videos or Log files with your request**  
    Logs, Screenshots and Videos are essential for us to understand the runtime environment, identify potential errors, and pinpoint the source of issues. We cannot provide effective support without them.  
    
5. **Check the Example Projects**  
    Each Asset we provide includes an example project demonstrating basic functionality and proper setup. This is often the quickest way to verify your own setup or understand how a feature is intended to work.
    - For example, if your character is not interacting with the foliage in your level, try play our demonstration level with your character in it to see if it works. This helps skip a few steps in determining the cause of the issue.

---

## **Where to Find Your Logs**

Logs are always generated in your project's Saved directory. The exact file names may vary, but the principle remains the same.

**Path:** YourProjectDirectory/Saved/Logs/

_(Add a clear screenshot here showing the typical_ _Saved/Logs_ _directory structure within an Unreal Engine project, with some example log files highlighted.)_

**Which log file should I include?**

- **IN EDITOR (PIE - Play In Editor):**  
    If you are running a PIE instance (e.g., "Play" button in the editor), you will typically find logs named something like YourProjectName.log. This will contain editor-specific information.
- **STANDALONE GAME (Editor):**  
    If you are running a Standalone Game instance directly from the editor, Unreal Engine will generate a separate log file for that specific instance, often named YourProjectName_2.log, YourProjectName_3.log, etc., for subsequent runs.
- **PACKAGED PROJECT:**  
    For packaged projects, logs are saved within the Saved directory of your packaged build. For example:  
    YourGame/Windows/YourProjectName/Saved/Logs/  
    The primary log file will typically be YourProjectName.log.