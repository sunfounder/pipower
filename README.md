# Pipower

PiPower code examples

## Usage

### Download the code
Get code from github

```bash
git clone https://github.com/sunfounder/pipower.git
cd pipower/examples
```
### Setup Pins
The default pin setup is:
```python
VUSB_PIN = 17
CHG_PIN = 18
LO_DT_PIN = 27
```
Change pin setup in the code if you need to.
```bash
# Change pin setup in the read_all.py
nano read_all.py
# Change pin setup in the safe_shutdown.py
nano safe_shutdown.py
```

### Check all status

```bash
cd pipower/examples
python3 read_all.py
```

### Test run safe shutdown

```bash
python3 safe_shutdown.py
```

## Setup safe shutdown on boot

Run this script will setup the safe shutdown on boot for you. This script will:
1. Copy the `safe_shutdown.py` to `/usr/local/bin/` as `pipower_safe_shutdown`
2. Give it executable permission
3. Copy service file for `pipower_safe_shutdown` to run on boot
4. Reload systemd daemon for the service to take effect

```bash
sudo bash enable_safe_shutdown.sh
```

You can add some code actions in `safe_shutdown.py` under `# Do some stuff before shutting down` to do something before shutdown. Like send a notification to your phone, or close some services if needed.

Remember to run `enable_safe_shutdown.sh` again if you change the `safe_shutdown.py` file.

```bash
sudo bash enable_safe_shutdown.sh
```
