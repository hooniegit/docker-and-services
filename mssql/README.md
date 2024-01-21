# installation for ARM MacOS / AMD Ubuntu
``` shell
$ docker pull mcr.microsoft.com/azure-sql-edge

# can't use "!" at password
$ docker run \
-e "ACCEPT_EULA=1" \
-e "MSSQL_SA_PASSWORD=<password>" \
-p 1433:1433 \
--name mssql-server \
-d mcr.microsoft.com/azure-sql-edge
```
<br><br>

# download official IDE
- `username` == `sa`
- set `Encrypt` as `Optional (False)` for connection
<br>
https://learn.microsoft.com/en-us/azure-data-studio/download-azure-data-studio?view=sql-server-ver15&tabs=macOS-install%2Cwin-user-install%2Credhat-install%2Cwindows-uninstall%2Credhat-uninstall

