fswatch -o . | (while read; do echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"; /usr/bin/env python3 -m unittest discover -s test; done)
