# -*- coding: utf-8 -*-
info = {
    "name": "ja",
    "date_order": "YMD",
    "january": [
        "1月",
        "一月"
    ],
    "february": [
        "2月",
        "二月"
    ],
    "march": [
        "3月",
        "三月"
    ],
    "april": [
        "4月",
        "四月"
    ],
    "may": [
        "5月",
        "五月"
    ],
    "june": [
        "6月",
        "六月"
    ],
    "july": [
        "7月",
        "七月"
    ],
    "august": [
        "8月",
        "八月"
    ],
    "september": [
        "9月",
        "九月"
    ],
    "october": [
        "10月",
        "十月"
    ],
    "november": [
        "11月",
        "十一月"
    ],
    "december": [
        "12月",
        "十二月"
    ],
    "monday": [
        "月曜日",
        "月",
        "(月)"
    ],
    "tuesday": [
        "火曜日",
        "火",
        "(火)"
    ],
    "wednesday": [
        "水曜日",
        "水",
        "(水)"
    ],
    "thursday": [
        "木曜日",
        "木",
        "(木)"
    ],
    "friday": [
        "金曜日",
        "金",
        "(金)"
    ],
    "saturday": [
        "土曜日",
        "土",
        "(土)"
    ],
    "sunday": [
        "日曜日",
        "日",
        "(日)"
    ],
    "am": [
        "午前"
    ],
    "pm": [
        "午後"
    ],
    "year": [
        "年"
    ],
    "month": [
        "月",
        "ヶ月",
        "カ月",
        "か月"
    ],
    "week": [
        "週",
        "週間"
    ],
    "day": [
        "日",
        "日間"
    ],
    "hour": [
        "時",
        "時間"
    ],
    "minute": [
        "分",
        "分間"
    ],
    "second": [
        "秒",
        "秒間"
    ],
    "relative-type": {
        "1 year ago": [
            "昨年"
        ],
        "0 year ago": [
            "今年"
        ],
        "in 1 year": [
            "翌年"
        ],
        "1 month ago": [
            "先月"
        ],
        "0 month ago": [
            "今月"
        ],
        "in 1 month": [
            "翌月"
        ],
        "1 week ago": [
            "先週"
        ],
        "0 week ago": [
            "今週"
        ],
        "in 1 week": [
            "翌週"
        ],
        "1 day ago": [
            "昨日"
        ],
        "0 day ago": [
            "今日"
        ],
        "in 1 day": [
            "明日"
        ],
        "0 hour ago": [
            "1 時間以内"
        ],
        "0 minute ago": [
            "1 分以内"
        ],
        "0 second ago": [
            "今"
        ]
    },
    "relative-type-regex": {
        "in \\1 year": [
            "(\\d+) 年後",
            "(\\d+)年後"
        ],
        "\\1 year ago": [
            "(\\d+) 年前",
            "(\\d+)年前"
        ],
        "in \\1 month": [
            "(\\d+) か月後",
            "(\\d+)か月後"
        ],
        "\\1 month ago": [
            "(\\d+) か月前",
            "(\\d+)か月前"
        ],
        "in \\1 week": [
            "(\\d+) 週間後",
            "(\\d+)週間後"
        ],
        "\\1 week ago": [
            "(\\d+) 週間前",
            "(\\d+)週間前"
        ],
        "in \\1 day": [
            "(\\d+) 日後",
            "(\\d+)日後"
        ],
        "\\1 day ago": [
            "(\\d+) 日前",
            "(\\d+)日前"
        ],
        "in \\1 hour": [
            "(\\d+) 時間後",
            "(\\d+)時間後"
        ],
        "\\1 hour ago": [
            "(\\d+) 時間前",
            "(\\d+)時間前"
        ],
        "in \\1 minute": [
            "(\\d+) 分後",
            "(\\d+)分後"
        ],
        "\\1 minute ago": [
            "(\\d+) 分前",
            "(\\d+)分前"
        ],
        "in \\1 second": [
            "(\\d+) 秒後",
            "(\\d+)秒後"
        ],
        "\\1 second ago": [
            "(\\d+) 秒前",
            "(\\d+)秒前"
        ]
    },
    "locale_specific": {},
    "no_word_spacing": "True",
    "skip": [
        "約",
        " ",
        ".",
        ",",
        ";",
        "-",
        "/",
        "'",
        "|",
        "@",
        "[",
        "]",
        "，"
    ],
    "ago": [
        "前"
    ],
    "in": [
        "今から",
        "で"
    ],
    "simplifications": [
        {
            "(\\d+)年(?:\\s+)?(\\d+)月(?:\\s+)?(\\d+)日": "\\1-\\2-\\3"
        },
        {
            "(\\d+)月(?:\\s+)?(\\d+)日": "\\1-\\2"
        },
        {
            "(\\d+)時(?:\\s+)?(\\d+)分(?:\\s+)?(\\d+)秒": "\\1:\\2:\\3"
        },
        {
            "(\\d+)時(?:\\s+)?(\\d+)分": "\\1:\\2"
        },
        {
            "(\\d+)時$": "\\1:00"
        },
        {
            "1月": "一月"
        },
        {
            "2月": "二月"
        },
        {
            "3月": "三月"
        },
        {
            "4月": "四月"
        },
        {
            "5月": "五月"
        },
        {
            "6月": "六月"
        },
        {
            "7月": "七月"
        },
        {
            "8月": "八月"
        },
        {
            "9月": "九月"
        },
        {
            "10月": "十月"
        },
        {
            "11月": "十一月"
        },
        {
            "12月": "十二月"
        },
        {
            "先々": 2
        },
        {
            "一昨": 2
        },
        {
            "去": 1
        },
        {
            "昨": 1
        },
        {
            "先": 1
        },
        {
            "今": 0
        },
        {
            "現在": "now"
        }
    ]
}