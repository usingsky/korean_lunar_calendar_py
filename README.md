<h1 align="center">korean_lunar_calendar</h1>

<p align="center">
  Convert between the <strong>Korean lunar calendar</strong> (음력) and the
  <strong>Gregorian solar calendar</strong> (양력) — entirely offline, following the
  <a href="https://astro.kasi.re.kr/">KARI</a> (Korea Astronomy and Space Science Institute) standard.
</p>

<p align="center">
  <a href="https://pypi.org/project/korean_lunar_calendar/"><img src="https://img.shields.io/pypi/v/korean_lunar_calendar.svg" alt="PyPI version" /></a>
  <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT license" />
  <img src="https://img.shields.io/badge/deps-zero-success.svg" alt="Zero dependencies" />
  <a href="https://usingsky.github.io/korean_lunar_calendar_js"><img src="https://img.shields.io/badge/demo-live-success.svg" alt="Live demo" /></a>
</p>

> The Korean and Chinese lunar calendars share the same astronomical basis but can fall on
> different dates. This library uses the Korean (KARI) standard.

## Features

- **Two-way conversion** — solar → lunar and lunar → solar.
- **Offline** — the conversion table is bundled; no network calls, no external services.
- **GapJa (간지) strings** — the sexagenary year/month/day in both Korean (정유년 병오월) and Chinese (丁酉年 丙午月).
- **Leap-month aware** — handles intercalation months (윤달) and the 1582 Gregorian reform gap.
- **Input validation** — every setter returns a `bool`; out-of-range, non-integer, and impossible-leap-month dates are rejected.
- **Pure standard library** — no third-party dependencies.

## Supported range

| Calendar     | From         | To           |
| ------------ | ------------ | ------------ |
| Lunar (음력)  | `1000-01-01` | `2050-11-18` |
| Solar (양력)  | `1000-02-13` | `2050-12-31` |

Dates outside this range cause the corresponding setter to return `False`.

## Install

```bash
pip install korean_lunar_calendar
```

```python
from korean_lunar_calendar import KoreanLunarCalendar
```

## Usage

### Solar → Lunar (양력 → 음력)

```python
calendar = KoreanLunarCalendar()

# setSolarDate(year, month, day) -> bool
calendar.setSolarDate(2017, 6, 24)

print(calendar.LunarIsoFormat())        # 2017-05-01 Intercalation
print(calendar.getGapJaString())        # 정유년 병오월 임오일 (윤월)
print(calendar.getChineseGapJaString()) # 丁酉年 丙午月 壬午日 (閏月)
```

### Lunar → Solar (음력 → 양력)

```python
calendar = KoreanLunarCalendar()

# setLunarDate(year, month, day, isIntercalation) -> bool
calendar.setLunarDate(1956, 1, 21, False)

print(calendar.SolarIsoFormat())  # 1956-03-03
print(calendar.getGapJaString())  # 병신년 경인월 기사일

# Intercalation (leap) month, e.g. lunar 1727-03-01 (leap) -> solar 1727-04-21
calendar.setLunarDate(1727, 3, 1, True)
print(calendar.SolarIsoFormat())  # 1727-04-21
print(calendar.getGapJaString())  # 정미년 갑진월 정사일 (윤월)
```

> Always check the return value of `setSolarDate` / `setLunarDate` before reading the result —
> the accessors reflect the **last successful** set call.

## API

`KoreanLunarCalendar()` creates a stateful converter. Set a date, then read it back in the
other calendar.

| Member | Returns | Description |
| ------ | ------- | ----------- |
| `setSolarDate(year, month, day)` | `bool` | Set a Gregorian date. Returns `False` for out-of-range, non-integer, or nonexistent dates. |
| `setLunarDate(year, month, day, isIntercalation)` | `bool` | Set a lunar date. `isIntercalation` requests the leap month; returns `False` if that month has no leap month. |
| `LunarIsoFormat()` | `str` | Lunar date as `YYYY-MM-DD`, with ` Intercalation` appended for a leap month. |
| `SolarIsoFormat()` | `str` | Solar date as `YYYY-MM-DD`. |
| `getGapJaString()` | `str` | Sexagenary cycle in Korean, e.g. `정유년 병오월 임오일 (윤월)`. |
| `getChineseGapJaString()` | `str` | Sexagenary cycle in Chinese characters, e.g. `丁酉年 丙午月 壬午日 (閏月)`. |

After a successful set you can also read the components directly:
`lunarYear`, `lunarMonth`, `lunarDay`, `isIntercalation`, `solarYear`, `solarMonth`, `solarDay`.

## Validation

Every setter validates its input and returns a `bool`, so you can branch on the result:

```python
calendar = KoreanLunarCalendar()

# Rejected -> returns False
calendar.setLunarDate(99, 1, 1, False)    # before supported range
calendar.setSolarDate(2051, 1, 1)         # after supported range
calendar.setSolarDate(2017, 6, 24.5)      # non-integer input
calendar.setSolarDate(1582, 10, 8)        # skipped by the 1582 Gregorian reform
calendar.setLunarDate(2017, 3, 1, True)   # month 3 of 2017 has no leap month

# Accepted -> returns True
calendar.setLunarDate(1000, 1, 1, False)
calendar.setSolarDate(2050, 12, 31)
```

## Tests

```bash
python -m unittest -v
```

## Other languages

- **Java** — [usingsky/KoreanLunarCalendar](https://github.com/usingsky/KoreanLunarCalendar)
- **Python** — [usingsky/korean_lunar_calendar_py](https://github.com/usingsky/korean_lunar_calendar_py)
- **JavaScript** — [usingsky/korean_lunar_calendar_js](https://github.com/usingsky/korean_lunar_calendar_js)

## Acknowledgements

Conversion data follows the [KARI (Korea Astronomy and Space Science Institute)](https://astro.kasi.re.kr/)
Korean lunar–solar standard. Many thanks to KARI for publishing the reference tables.

## License

MIT © [Jinil Lee](https://github.com/usingsky)
