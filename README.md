# korean_lunar_calendar_py
한국 양음력 변환

#### Overview
Here is a library to convert Korean lunar-calendar to Gregorian calendar.

Korean calendar and Chinese calendar is same lunar calendar but have different date.

This follow the KARI(Korea Astronomy and Space Science Institute)

한국 양음력 변환 (한국천문연구원 기준) - 네트워크 연결 불필요

음력 변환은 1391년 1월 1일 부터 2050년 11월 18일까지 지원

````
Gregorian calendar (1391. 2. 5. ~ 2050. 12. 31) <--> Korean lunar-calendar (1391. 1. 1. ~ 2050. 11. 18)
````
#### Install

pip install korean_lunar_calendar

#### To use

from korean_lunar_calendar import KoreanLunarCalendar

(1) Korean Lunar Date -> Korean Solar Date (음력 -> 양력)
```python
calendar = KoreanLunarCalendar()
# year(년), month(월), day(일),
calendar.setSolarDate(1392, 2, 23);
```

```
=> 1391. 3. 3.
```
(2) Korean Solar Date -> Korean Lunar Date (양력 -> 음력)
```python
calendar = KoreanLunarCalendar()
# year(년), month(월), day(일), intercalation(윤달여부)
calendar.setLunarDate(2018, 1, 21, False); 
```

```
=> 2019. 1. 24.
```

(3) Getting Korean GapJa String (음력간지)
```python
calendar.getGapJaString()
```

```
무술년 갑인월 기해일
```
