from __future__ import annotations

import os

from ckanext.theming.lib import Theme

here = os.path.dirname(__file__)

icon_map = {
    "bars": "☰",
    "battery-empty": "🪫",
    "battery-full": "🔋",
    "battery-half": "🪫",
    "bell": "🔔",
    "bell-slash": "🔕",
    "bookmark": "🔖",
    "calendar": "📅",
    "calendar-alt": "🗓️",
    "chart-area": "📉",
    "chart-bar": "📊",
    "chart-line": "📈",
    "chart-pie": "🥧",
    "chart-scatter": "📊",
    "check": "✔️",  # Success / confirmation
    "check-circle": "✅",
    "chevron-down": "▾",  # Expand
    "chevron-left": "◂",  # Back
    "chevron-right": "▸",  # Forward
    "chevron-up": "▴",  # Collapse
    "clipboard": "📋",
    "clock": "⏰",
    "cloud": "☁️",
    "cloud-download-alt": "☁️⬇️",
    "cloud-upload-alt": "☁️⬆️",
    "cog": "⚙️",  # Settings / configuration
    "cogs": "🛠️",
    "comment": "💬",
    "comments": "🗨️",
    "copy": "📋",
    "database": "🗄️",
    "download": "⬇️",  # Download
    "download-alt": "⤵️",
    "edit": "✏️",  # Edit / update
    "ellipsis-h": "⋯",
    "ellipsis-v": "⋮",
    "envelope": "✉️",
    "envelope-open": "📬",
    "exclamation-triangle": "⚠️",  # Warning
    "external-link-alt": "🌐",
    "eye": "👁️",  # View / show
    "eye-slash": "🙈",
    "file": "📄",
    "file-alt": "📄",
    "file-csv": "📑",
    "file-excel": "📊",
    "file-pdf": "📕",
    "filter": "🧹",
    "folder": "📁",
    "folder-open": "📂",
    "globe": "🌍",
    "heart": "❤️",
    "home": "🏠",  # Home navigation
    "info": "ℹ",
    "info-circle": "ℹ️",  # Information / help
    "key": "🔑",
    "language": "🈯",
    "link": "🔗",
    "list": "📋",
    "list-alt": "🗒️",
    "lock": "🔒",  # Locked / secure
    "map": "🗺️",
    "map-marker-alt": "📍",
    "minus": "➖",  # Remove / reduce
    "pause": "⏸️",
    "play": "▶️",
    "plus": "➕",  # Add / create
    "print": "🖨️",
    "question-circle": "❓",
    "redo": "↪️",
    "save": "💾",
    "search": "🔍",  # Search functionality
    "share": "🔗",
    "shield-alt": "🛡️",
    "signal": "📡",
    "sliders-h": "🎚️",
    "sliders-v": "🎛️",
    "sort": "↕️",
    "sort-down": "⬇️",
    "sort-up": "⬆️",
    "star": "⭐",
    "star-half": "🌗",
    "stop": "⏹️",
    "sync": "🔄",
    "table": "🗂️",
    "tag": "🏷️",
    "thumbs-down": "👎",
    "thumbs-up": "👍",
    "times": "❌",  # Close / cancel
    "times-circle": "⛔",
    "trash": "🗑️",  # Delete / trash
    "trash-alt": "🚮",
    "undo": "↩️",
    "unlock": "🔓",  # Unlocked / open
    "upload": "⬆️",  # Upload
    "upload-alt": "⤴️",
    "user": "👤",  # User / profile
    "users": "👥",
    "wifi": "📶",
}


def make_theme():
    return Theme("bare", here, icon_map=icon_map)
