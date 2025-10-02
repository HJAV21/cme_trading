import os

# Base project path
base_path = r"OneDrive/Documents/Project Work/cme_trading"

# Folder structure
folders = [
    "config",
    "data/raw",
    "data/processed",
    "data/features",
    "notebooks",
    "src",
    "src/data",
    "src/models",
    "src/meta",
    "src/execution",
    "src/retraining",
    "src/monte_carlo",
    "src/utils",
    "logs",
    "tests",
    "scripts"
]

# Files to create
files = [
    "README.md",
    "requirements.txt",
    "config/settings.yaml",
    "config/regimes.yaml",
    "config/risk_params.yaml",
    "src/__init__.py",
    "src/main.py",
    "logs/trade_signals.csv",
    # src/data
    "src/data/data_loader.py",
    "src/data/feature_engineer.py",
    "src/data/data_utils.py",
    # src/models
    "src/models/ta_models.py",
    "src/models/ml_models.py",
    "src/models/dl_models.py",
    "src/models/stochastic_models.py",
    "src/models/entropy_models.py",
    "src/models/game_theory_models.py",
    # src/meta
    "src/meta/ensemble.py",
    "src/meta/regime_detector.py",
    "src/meta/bandit_controller.py",
    # src/execution
    "src/execution/execution_engine.py",
    "src/execution/order_slicer.py",
    "src/execution/risk_manager.py",
    "src/execution/slippage_model.py",
    # src/retraining
    "src/retraining/retrain_manager.py",
    "src/retraining/shadow_test.py",
    "src/retraining/model_updater.py",
    # src/monte_carlo
    "src/monte_carlo/monte_carlo_sim.py",
    # src/utils
    "src/utils/logger.py",
    "src/utils/visualization.py",
    "src/utils/config_loader.py",
    "src/utils/notifications.py",
    # tests
    "tests/test_data.py",
    "tests/test_models.py",
    "tests/test_meta.py",
    "tests/test_execution.py",
    # scripts
    "scripts/backtest.py",
    "scripts/retrain.py",
    "scripts/monitor.py"
]

# Create folders
for folder in folders:
    folder_path = os.path.join(base_path, folder)
    os.makedirs(folder_path, exist_ok=True)

# Create files
for file in files:
    file_path = os.path.join(base_path, file)
    if not os.path.exists(file_path):
        open(file_path, 'a').close()

print(f"Project structure created at {base_path}")
