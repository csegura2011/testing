# Notes on Webservices with Python

## About this Document 
* Author: Cristian Segura [cristian.segura.lepe@gmail.com](cristian.segura.lepe@gmail.com)
* Creation Date: 2017/03/28

## References

* Python for Informatics Chapter 13; [Youtube Video](https://www.youtube.com/watch?v=6cwi1NcL0Zc)


## Introduction



## 1.- XML

### 1.1 XML Basics




`SLIDE 01`

* Start tag
* End Tag
* Text Content
* Attribute
* Self Closing Tag


```xml
<person>        # Start "person" tag
<name>Chuck</name> 
<phone type="intl">+1 734 303 4456</phone>
<email hide="yes"></email>
</person>       # --> End "person" Tag
```

`SLIDE 02`

* White Space
    - Line ends do no matter
    - White space is generally discarded on text elements
    - We indent only to be readable

```xml
<person>
    <name>Chuck</name> 
          <phone type="intl">+1 734 303 4456</phone>
                  <email hide="yes"></email>
</person>
```





