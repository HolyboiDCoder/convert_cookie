# convert_cookie
This Python script is a tool for converting cookies from a .json format to the Netscape format. The purpose of the conversion is to facilitate the import of cookies into another web browser that supports the Netscape format.

Here's a breakdown of what the script does:
1. It imports required modules, including colorama for colored output on the console.
2. The script defines various color codes using colorama for more visually appealing console output.
3. It imports the json module to handle the .json cookie file.
4. The function convert_to_netscape takes the name of the .json cookie file and the output file as input.
5. The script reads the .json cookie file and loads the data into the cookie_data variable.
6. It then iterates through each cookie in the cookie_data dictionary and extracts the cookie domain and value.
7. The extracted cookie data is then formatted into the Netscape cookie format: domain\tTRUE\t/\tFALSE\t0\tname\tvalue.
8. The formatted Netscape cookies are written to the output file.
9. The user is notified when the conversion is completed and asked to press Enter to exit.


Overall, this script is a useful tool for converting cookies between different formats, making it easier to import cookies into other web browsers that support the Netscape cookie format.

The export_cookie.json file is the .json file that we want to convert to Netscape cookie format.
