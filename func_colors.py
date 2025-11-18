from __future__ import annotations

from typing import Iterable

import numpy as np
import matplotlib.cm as mcm
from matplotlib.colors import to_hex, Colormap

# cmcrameri는 선택적(optional) 의존성으로 처리
try:
    from cmcrameri import cm as _cmcrameri
except ImportError:  # 패키지가 없으면 None으로 두고 넘어감
    _cmcrameri = None


def get_color_array(
    cmap: str | Colormap,
    data_length: int,
    *,
    c_start: float = 0.075,
    c_end: float = 1.0,
) -> np.ndarray:
    """
    주어진 colormap에서 `data_length`만큼 색을 샘플링하여 RGBA 배열 반환.

    Parameters
    ----------
    cmap : str 또는 Colormap
        - str 이면:
          1) cmcrameri.cm 안에서 먼저 찾고
          2) 없으면 matplotlib.cm.get_cmap 에서 찾는다.
        - Colormap 인스턴스면 그대로 사용.
    data_length : int
        샘플링할 색 개수.
    c_start, c_end : float
        colormap 상에서 사용할 구간 (0~1).

    Returns
    -------
    colors : (N, 4) ndarray
        RGBA 배열 (0~1 범위).
    """
    if isinstance(cmap, Colormap):
        cmap_obj = cmap
    elif isinstance(cmap, str):
        cmap_obj = None

        # 1) cmcrameri 우선
        if _cmcrameri is not None and hasattr(_cmcrameri, cmap):
            cmap_obj = getattr(_cmcrameri, cmap)
        else:
            # 2) matplotlib 기본 colormap
            cmap_obj = mcm.get_cmap(cmap)

    else:
        raise TypeError("cmap 은 str 또는 matplotlib.colors.Colormap 이어야 합니다.")

    values = np.linspace(c_start, c_end, data_length)
    return cmap_obj(values)


def rgb2hex(color: Iterable[float]) -> str:
    """
    (r, g, b) 또는 (r, g, b, a) 형태의 색을 16진수 문자열로 변환.
    입력 값은 0~1 범위 혹은 0~255 범위 모두 허용.

    Examples
    --------
    >>> rgb2hex((1.0, 0.5, 0.0))
    '#ff8000'
    """
    arr = np.array(list(color), dtype=float).ravel()
    if arr.size < 3:
        raise ValueError("rgb2hex: 최소 3개 값(r,g,b)이 필요합니다.")

    # 0~255 범위로 들어왔으면 0~1 로 정규화
    if arr.max() > 1.0:
        arr = arr / 255.0

    # 앞의 3개(r,g,b)만 사용, to_hex가 '#rrggbb' 반환
    return to_hex(arr[:3], keep_alpha=False)


# ----------------------------------------------------------------------
# 고정 팔레트 색상 (논문/프레젠용)
# ----------------------------------------------------------------------
c_red = "#FF2C43"
c_orange = "#FF9A47"
c_yellow = "#F8E448"
c_lime = "#98EE84"
c_green = "#1B9C21"
c_mint = "#76DDBE"
c_blue = "#49BCE6"
c_navy = "#4965E6"
c_purple = "#A588DB"
c_pink = "#FF7BCC"
