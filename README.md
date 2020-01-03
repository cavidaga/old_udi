# Simple translit tool

## Usage

```
$ python3 main.py --infile mingechaur.txt
𐕂𐔼𐔺𐔰𐕚 𐕃𐔶 𐔱𐔴𐕐𐔼𐔺𐕚𐔼 𐕒𐔾𐕒𐔰𐕙𐔰𐕆𐔶𐕎𐔴 𐔴 𐔼! = 𐕚'𐔼𐔺𐔰𐕚 𐕃𐔶 𐔱𐔴𐕐𐔼𐔺𐕚𐔼 𐕒𐔾𐕒𐔰𐕙𐔰𐕆𐔶𐕎𐔴 𐔴 𐔼!
𐕆𐔰𐔾 𐔺𐔶 𐕒𐕛𐕚𐔴𐕎𐔰 𐕀𐕒𐕚𐕙𐕒𐕒𐕡𐔼 = 𐕆𐔰𐔾 𐔺𐔶 𐕒𐕛𐕚𐔴𐕎𐔰 𐕀𐕒𐕚𐕙𐕒𐕒𐕞𐕛𐔼
```

and otherway:

```
$ python3 main.py --infile mingechaur.txt --udi-to-albanian
S'ǏYAS ĈĔ BEŞǏYSǏ ŎLŎARAHĔNE E Ǐ! = S'İYAS ĈƏ BEŞİYSİ OLOARAHƏNE E İ!
HAL YĔ ŎVSENA XŎSRŎŎ𐕡Ǐ = HAL YƏ OVSENA XOSROOUVİ
```

_If you want to save result printed to the screen but to a file, do:_

```
$ python3 main.py --infile mingechaur.txt --udi-to-albanian > some_file.txt
```
