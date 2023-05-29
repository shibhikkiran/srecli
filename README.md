# Srecli

`srecli` is a click based CLI tool to cater common SRE related system automation tasks.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install `srecli`.

```bash
pip install srecli
```

## Usage
#### Show status
```bash
srecli show status
2023/05/29 15:41:44 UTC | INFO     | This is info msg
2023/05/29 15:41:44 UTC | WARNING  | This is warning msg
2023/05/29 15:41:44 UTC | ERROR    | This is error msg
2023/05/29 15:41:44 UTC | CRITICAL | This is critical msg
2023/05/29 15:41:44 UTC | SUCCESS  | This is success msg
echo msg: Hello
```
#### Show status with debug 
```bash
srecli show status --debug
2023/05/29 15:43:45 UTC | DEBUG    | srecli.commands.cmd_status.show:39 | PID=1966 | This is debug msg
2023/05/29 15:43:47 UTC | INFO     | srecli.commands.cmd_status.show:41 | PID=1966 | This is info msg
2023/05/29 15:43:47 UTC | WARNING  | srecli.commands.cmd_status.show:42 | PID=1966 | This is warning msg
2023/05/29 15:43:47 UTC | ERROR    | srecli.commands.cmd_status.show:43 | PID=1966 | This is error msg
2023/05/29 15:43:47 UTC | CRITICAL | srecli.commands.cmd_status.show:44 | PID=1966 | This is critical msg
2023/05/29 15:43:47 UTC | SUCCESS  | srecli.commands.cmd_status.show:45 | PID=1966 | This is success msg
echo msg: Hello
```
#### Show status with custom message
```bash
srecli show status --echo-msg "Hello from Srecli"
2023/05/29 15:41:44 UTC | INFO     | This is info msg
2023/05/29 15:41:44 UTC | WARNING  | This is warning msg
2023/05/29 15:41:44 UTC | ERROR    | This is error msg
2023/05/29 15:41:44 UTC | CRITICAL | This is critical msg
2023/05/29 15:41:44 UTC | SUCCESS  | This is success msg
echo msg: Hello from Srecli
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
