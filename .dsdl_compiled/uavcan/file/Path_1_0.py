# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/pi/CyphalDemo/public_regulated_data_types/uavcan/file/Path.1.0.dsdl
#
# Generated at:  2022-05-18 08:39:25.971086 UTC
# Is deprecated: yes
# Fixed port ID: None
# Full name:     uavcan.file.Path
# Version:       1.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import warnings as _warnings_


def _restore_constant_(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class Path_1_0:
    """
    Generated property settings use relaxed type signatures, accepting a large variety of
    possible representations of the value, which are automatically converted to a well-defined
    internal representation. When accessing a property, this strict well-defined internal
    representation is always returned. The implicit strictification enables more precise static
    type analysis.

    The value returned by the __repr__() method may be invariant to some of the field values,
    and its format is not guaranteed to be stable. Therefore, the returned string representation
    can be used only for displaying purposes; any kind of automation build on top of that will
    be fragile and prone to mismaintenance.
    """
    SEPARATOR:  int = 47
    MAX_LENGTH: int = 112

    def __init__(self,
                 path: None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str = None) -> None:
        """
        uavcan.file.Path.1.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param path: saturated uint8[<=112] path
        """
        _warnings_.warn('Data type uavcan.file.Path.1.0 is deprecated', DeprecationWarning)

        self._path: _NDArray_[_np_.uint8]

        if path is None:
            self.path = _np_.array([], _np_.uint8)
        else:
            path = path.encode() if isinstance(path, str) else path  # Implicit string encoding
            if isinstance(path, (bytes, bytearray)) and len(path) <= 112:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._path = _np_.frombuffer(path, _np_.uint8)  # type: ignore
            elif isinstance(path, _np_.ndarray) and path.dtype == _np_.uint8 and path.ndim == 1 and path.size <= 112:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._path = path
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                path = _np_.array(path, _np_.uint8).flatten()
                if not path.size <= 112:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'path: invalid array length: not {path.size} <= 112')
                self._path = path
            assert isinstance(self._path, _np_.ndarray)
            assert self._path.dtype == _np_.uint8  # type: ignore
            assert self._path.ndim == 1
            assert len(self._path) <= 112

    @property
    def path(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[<=112] path
        DSDL does not support strings natively yet. To interpret this array as a string,
        use tobytes() to convert the NumPy array to bytes, and then decode() to convert bytes to string:
        .path.tobytes().decode()
        When assigning a string to this property, no manual conversion is necessary (it will happen automatically).
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._path

    @path.setter
    def path(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray | str) -> None:
        x = x.encode() if isinstance(x, str) else x  # Implicit string encoding
        if isinstance(x, (bytes, bytearray)) and len(x) <= 112:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._path = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size <= 112:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._path = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size <= 112:  # Length cannot be checked before casting and flattening
                raise ValueError(f'path: invalid array length: not {x.size} <= 112')
            self._path = x
        assert isinstance(self._path, _np_.ndarray)
        assert self._path.dtype == _np_.uint8  # type: ignore
        assert self._path.ndim == 1
        assert len(self._path) <= 112

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        # Variable-length array: length field byte-aligned: True; all elements byte-aligned: True.
        assert len(self.path) <= 112, 'self.path: saturated uint8[<=112]'
        _ser_.add_aligned_u8(len(self.path))
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.path)
        _ser_.pad_to_alignment(8)
        assert 8 <= (_ser_.current_bit_length - _base_offset_) <= 904, \
            'Bad serialization of uavcan.file.Path.1.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> Path_1_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "path"
        # Length field byte-aligned: True; all elements byte-aligned: True.
        _len0_ = _des_.fetch_aligned_u8()
        assert _len0_ >= 0
        if _len0_ > 112:
            raise _des_.FormatError(f'Variable array length prefix {_len0_} > 112')
        _f0_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, _len0_)
        assert len(_f0_) <= 112, 'saturated uint8[<=112]'
        self = Path_1_0(
            path=_f0_)
        _des_.pad_to_alignment(8)
        assert 8 <= (_des_.consumed_bit_length - _base_offset_) <= 904, \
            'Bad deserialization of uavcan.file.Path.1.0'
        assert isinstance(self, Path_1_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'path=%s' % repr(bytes(self.path))[1:],
        ])
        return f'uavcan.file.Path.1.0({_o_0_})'

    _EXTENT_BYTES_ = 113

    _MODEL_: _pydsdl_.StructureType = _restore_constant_(
        'ABzY8y|9F00{?|pZEqAe5WbKEE=PgVv_<NRaHF=mNU#+8hWe@3K-%g^NJBuBidx>?xwFfjy|TTzT%}6zp%s-Z6$$tMc4qf3M}VmJ'
        'Wp~G(XJ(!mKfcFH|1Phz>R-56PI8wQ33p(XDAeyFEg<2U8I{H<4>6p%<877s%EI2Hg!nwJKZ$?DZdm48jBx$UO6+GsCj*6!JHpEt'
        '+I%0ZQ$|PG3a9Q(-=D|+LcjG_d=kTHF1)uYtvtB+5W$W~<8W6D%bN;{d>+2TbKwQ|lv8;B7<X&MB!&z31X|H@3-r*-9$Ampa)v_z'
        'BhY?|cT75^RU_rqKJHk(tDPEZ$bZxxhG384o#v_Xyr{#)ejAg`g!6o4a)|Q1@b1nGh}@D5T-%~0WT^FL+>POF?!3^su=$HXPpdSn'
        'AW|tZ<tMRUhPS3md_d$h$;%I#B;>_@TQa%UUm!^N33)H^v~V$eIxBAuj+OeCzhijgJLMbF?%?ONys*ek83Q{G#7#!2DO83eZNbPO'
        'c^=z;y96t|v2&76@=Pjhsr)>=vte{5Jm}YMrJ`x41x>?(`_FAxMIr3um7OQ~z9=e)|HN*;{miBE%PASx(d)vl&_mdT61+MtrAK@u'
        '4v<=O__j96jTu(W-$-d}620KIt;dVu6m_*K1o`(DXm9ITzui15Y&;y4Lf7-ZU8R5--Nv@;Y&~6+KfTUF-o<ScOD>0{vOY~qJU2*Y'
        'E28miXd_iL9Ea`b%GH-z{&C%G1X#IqbEmi4+q;eZe;|L68{xxQ(=aUyj`BJ(*6rQ81EQFrqtD8~ij1r{Iql8qJFbTlUwj>Dw(4{r'
        '{$Dbkt=@fp>*n_Ndp}IGkuVJ*e+!FOuU<O@gRuI7K=5?ZNDYDhEYHhS{wl516&|x3und}<JU$I)@faLH&P!uGS9#nH=eaYL&480Q'
        '@rKS*^e9w{W3_`4cTh{#b8P;?735kP(zFw$ilMVHDWxcG;0%+(R4L9hw=l$JW4yWiAT1{w4Mcwmgqlg9$<^eugxHRr&h#pm!eI`U'
        'WCnF*Uu6*gmJjZKwAgBGgF{S4a7m}f2!*)`+D44hWuP+@h@2_S?(S_~PuQLWW^^%OIPWTF4iK1TnJLFSt__SGqkJ$|2q)Rvl{JEO'
        'N)HLRwsq0C&MXX2o|!kbmo>(-Tp^_hHDO({6(*}^f|&suOO;6qk;6ct__1_S`%yVy*OSgJAUQZm4K8L4j&&g!CTuN9FdSCTG{u<u'
        'qsZ0YcoK00iGr>uyfoENA}|ITi3!Ujom;BCuB@WF2xH+v*hemDFj<#CKx5Sz<m=yb7`x1R4RxhaxJeJGM$s^fGznHH{fKN0*BG*B'
        'QUOe9tk6-+Sxt@yoU?_fwPgl8Uzwu69=SuUL^V;PYTE2ZOc4huA+j@R9B3vSI(jQ|xNHUkmVzGxn(3-W&Qn$3rO@E#0OgC}XBW65'
        'zB@$X*jVQ;<D~?Is2w(I8nzj&!`OH%vB`J}FHM^-io%Q?Jq|rFL!-S=nn)3|DO0sfWzfO7smp45%?!rJV8UWc=?r0cm44)!R$xp`'
        'vp6<vqqogAZ!i>}5x6AEOY%x17uSx6`nesE=NR!7F~`-f@SjN8EaNR)9o61LrA__=*wvS65D5SP'
    )
    assert isinstance(_MODEL_, _pydsdl_.StructureType)
