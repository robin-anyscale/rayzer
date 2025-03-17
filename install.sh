#!/bin/bash
set -e

echo "Installing Rayzer CLI..."

# Create a directory for the application
INSTALL_DIR="$HOME/.rayzer"
mkdir -p "$INSTALL_DIR"

# Install uv if not already installed
if ! command -v uv &> /dev/null; then
    echo "Installing uv package manager..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    # Add uv to PATH for this session
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# Check if repo directory already exists
if [ -d "$INSTALL_DIR/repo" ]; then
    echo "Repository already exists, updating..."
    cd "$INSTALL_DIR/repo"
    git pull
else
    echo "Cloning repository..."
    git clone git@github.com:robin-anyscale/rayzer.git "$INSTALL_DIR/repo"
    cd "$INSTALL_DIR/repo"
fi

# Install the project and its dependencies using uv
# echo "Installing project and dependencies..."
# uv pip install -e .

# Add typer and questionary if they're not already in pyproject.toml
uv pip install typer questionary

# Make scripts executable
chmod +x "$INSTALL_DIR/repo/ray_infra_local.sh"
chmod +x "$INSTALL_DIR/repo/ray_infra_aws.sh"
# chmod +x "$INSTALL_DIR/repo/ray_infra_anyscale.sh"

# Create a launcher script
cat > "$INSTALL_DIR/repo/rayzer" << EOF
#!/bin/bash
# Use the Python from the uv environment
$(which python) "$INSTALL_DIR/repo/main.py" rayzer "\$@"
EOF

chmod +x "$INSTALL_DIR/repo/rayzer"

# Create a symlink to make it available in PATH
mkdir -p "$HOME/.local/bin"
ln -sf "$INSTALL_DIR/repo/rayzer" "$HOME/.local/bin/rayzer"

echo "Installation complete!"
echo "Run 'rayzer' to start the application."

# Check if ~/.local/bin is in PATH, if not provide instructions
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo "" 
    echo "NOTE: Please add ~/.local/bin to your PATH to run rayzer from anywhere:"
    echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
    echo "You can add this line to your ~/.bashrc or ~/.zshrc file to make it permanent."
fi

# Run the application if --run flag is provided
if [[ "$1" == "--run" ]]; then
    echo ""
    echo "Starting Rayzer CLI..."
    
    # Check if we're in an interactive terminal
    if [ -t 0 ]; then
        # Interactive terminal, run normally
        $INSTALL_DIR/repo/rayzer
    else
        # Non-interactive terminal, show alternative instructions
        echo "Note: For the best experience, Rayzer should be run in an interactive terminal."
        echo "The CLI will attempt to run, but you may see warnings about 'Input is not a terminal'."
        echo ""
        echo "For a fully interactive experience, run this command in a regular terminal after installation:"
        echo "  rayzer"
        echo ""
        # Still try to run it, as it partially works
        rayzer
    fi
else
    echo ""
    echo "To start Rayzer now, run: rayzer"
fi
# # Run the application if --run flag is provided
# if [[ "$1" == "--run" ]]; then
#     echo ""
#     echo "Starting Rayzer CLI..."
#     rayzer
#     # # Check if we're in an interactive terminal
#     # if [ -t 0 ]; then
#     #     # Interactive terminal, run normally
#     #     "$INSTALL_DIR/repo/rayzer"
#     # else
#     #     # Non-interactive terminal, show instructions instead
#     #     echo "The Rayzer CLI requires an interactive terminal."
#     #     echo "Please run 'rayzer' manually after installation."
#     #     echo ""
#     #     echo "To run Rayzer, open a new terminal and type:"
#     #     echo "rayzer"
#     # fi
# fi