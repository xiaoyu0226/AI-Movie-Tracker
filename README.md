<h2>AI Movie Tracker</h2>

<h4>Overview</h4>

The AI Movie Tracker is a dynamic application designed to help users manage their movie watching experience. Utilizing AI capabilities, it provides personalized movie recommendations based on genre and organizes movie data into categories like "Watched," "To Watch," and "Currently Watching." This tool integrates a language model (ChatGPT), a SQLite database for storage, and a Flask web interface.

<h4>Features</h4>

- Uses ChatGPT to recommend movies based on specified genres, providing diverse suggestions for users.
- Categorizes movies into "Watched," "To Watch," and "Currently Watching" for better tracking.
- Built with Flask, the web interface allows users to add and view movie lists.
- Movie details are stored in a SQLite database for quick access and persistence.

<h4>How It Works</h4>

**Add Movies:**

Users can add a movie to their list by providing details like:
- Title
- Release Year
- Description
- Status (Watched, To Watch, Currently Watching)
- Progress (0–100%)

**AI-Powered Recommendations:**

Users can request movie recommendations by genre. 

**View and Manage Lists:**

The web interface displays movies organized by their status. Features include:
- Expandable panels with detailed movie descriptions.
- Progress tracking.
