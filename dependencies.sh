/bin/rm -f .pipPackageList
pip3 freeze > .pipPackageList

for P in pytest coverage radon
do
        /usr/bin/python2 find_package.py --package $P .pipPackageList
        case $? in
        1)
                echo "Python package $P not found, installing..."
        y="pip3 install $P"
        $y
                ;;
        2)
                echo "Python package $P needs upgrade, upgrading..."
        y="pip3 install --upgrade $P"
        $y
                ;;
        esac
done

/bin/rm -f .pipPackageList
