# Morph Theme for Cursor IDE

A custom dark theme created by Peter Preketes specifically for Cursor IDE (the AI-powered fork of VS Code). I wanted to make my own custom theme for coding and programming that combines a comfortable dark background with vibrant accent colors for better code readability.

## What We Built

This project is a custom theme extension for Cursor IDE that I created from scratch. Here's what we did:

1. **Set up the Extension Structure** - Created a proper extension with manifest (`package.json`) and theme configuration
2. **Designed a Color Palette** - Carefully selected colors for optimal contrast and reduced eye strain during long coding sessions
3. **Configured UI Elements** - Customized colors for the editor, sidebar, activity bar, status bar, terminal, and all UI components
4. **Added Syntax Highlighting** - Defined token colors for different code elements (keywords, functions, strings, etc.) across all programming languages
5. **Tested & Packaged** - Built the theme as a `.vsix` extension that can be installed in Cursor IDE

## Features

- **Deep Dark Background** (#1e1e2e) - Easy on the eyes for extended coding sessions
- **Vibrant Accent Colors** - Purple keywords, blue functions, green strings for clear code distinction
- **Semantic Highlighting Support** - Enhanced syntax highlighting using semantic tokens
- **Complete UI Theming** - Every interface element styled for consistency
- **Optimized for Multiple Languages** - Works great with Python, JavaScript, TypeScript, and more

## Color Palette

The Morph theme uses a carefully crafted color palette inspired by modern dark themes:

- **Background**: `#1e1e2e` - Deep dark blue
- **Foreground**: `#cdd6f4` - Soft white text
- **Purple**: `#cba6f7` - Keywords, imports
- **Blue**: `#89b4fa` - Functions, methods
- **Green**: `#a6e3a1` - Strings
- **Yellow**: `#f9e2af` - Classes, types
- **Red**: `#f38ba8` - Tags, errors
- **Cyan**: `#94e2d5` - Operators
- **Orange**: `#fab387` - Constants, numbers
- **Pink**: `#f5c2e7` - Regular expressions

## Installation for Cursor IDE

### Method 1: From Source (This Repository)
1. Clone this repository: `git clone https://github.com/PeterP22/morph-theme.git`
2. Create a symlink to Cursor's extensions folder:
   ```bash
   ln -sf /path/to/morph-theme ~/.cursor/extensions/morph-theme
   ```
3. Restart Cursor IDE completely
4. Enable the theme:
   - Open Command Palette: `Cmd+Shift+P` (Mac) or `Ctrl+Shift+P` (Windows/Linux)
   - Type "Preferences: Color Theme"
   - Select "Morph Dark"
   - Or use the shortcut: `Cmd+K Cmd+T` (Mac) or `Ctrl+K Ctrl+T` (Windows/Linux)

### Method 2: From VSIX Package
1. Download the `.vsix` file from the [Releases](https://github.com/PeterP22/morph-theme/releases) page
2. Install in Cursor using:
   ```bash
   cursor --install-extension morph-theme-0.0.1.vsix
   ```
   Or if `cursor` command is not available:
   ```bash
   code --install-extension morph-theme-0.0.1.vsix
   ```
3. Restart Cursor and select "Morph Dark" from the theme picker

## Development

To modify or enhance the theme:

1. Edit `themes/morph-dark-color-theme.json` for color changes
2. Test changes by reloading the editor window
3. Package with: `npm run package`

## Technical Details

- **Built for**: Cursor IDE / VS Code 1.90.0+
- **Theme Type**: Dark theme based on `vs-dark`
- **Semantic Highlighting**: Enabled for enhanced language support
- **File Structure**:
  - `package.json` - Extension manifest
  - `themes/morph-dark-color-theme.json` - Complete theme definition

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements!

## License

MIT License - See [LICENSE](LICENSE) file for details

## Author

Created by Peter Preketes

---

*Enjoy coding with the Morph theme!*