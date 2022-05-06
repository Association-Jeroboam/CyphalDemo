# AUTOGENERATED, DO NOT EDIT.
#
# Source file:
# /home/thomas/git/CyphalDemo/public_regulated_data_types/uavcan/pnp/8165.NodeIDAllocationData.2.0.dsdl
#
# Generated at:  2022-05-06 20:25:54.312835 UTC
# Is deprecated: no
# Fixed port ID: 8165
# Full name:     uavcan.pnp.NodeIDAllocationData
# Version:       2.0
#
# pylint: skip-file
# mypy: warn_unused_ignores=False

from __future__ import annotations

from typing import Any as _Issue110_
import numpy as _np_
from numpy.typing import NDArray as _NDArray_
import pydsdl as _pydsdl_
import uavcan.node


def _restore_constant(encoded_string: str) -> object:
    import pickle, gzip, base64
    return pickle.loads(gzip.decompress(base64.b85decode(encoded_string)))


# noinspection PyUnresolvedReferences, PyPep8, PyPep8Naming, SpellCheckingInspection, DuplicatedCode
class NodeIDAllocationData_2_0:
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
    def __init__(self,
                 node_id:   None | uavcan.node.ID_1_0 = None,
                 unique_id: None | _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray  = None) -> None:
        """
        uavcan.pnp.NodeIDAllocationData.2.0
        Raises ValueError if any of the primitive values are outside the permitted range, regardless of the cast mode.
        :param node_id:   uavcan.node.ID.1.0 node_id
        :param unique_id: saturated uint8[16] unique_id
        """
        self._node_id:   uavcan.node.ID_1_0
        self._unique_id: _NDArray_[_np_.uint8]

        if node_id is None:
            self.node_id = uavcan.node.ID_1_0()
        elif isinstance(node_id, uavcan.node.ID_1_0):
            self.node_id = node_id
        else:
            raise ValueError(f'node_id: expected uavcan.node.ID_1_0 '
                             f'got {type(node_id).__name__}')

        if unique_id is None:
            self.unique_id = _np_.zeros(16, _np_.uint8)
        else:
            if isinstance(unique_id, (bytes, bytearray)) and len(unique_id) == 16:
                # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
                # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
                self._unique_id = _np_.frombuffer(unique_id, _np_.uint8)  # type: ignore
            elif isinstance(unique_id, _np_.ndarray) and unique_id.dtype == _np_.uint8 and unique_id.ndim == 1 and unique_id.size == 16:  # type: ignore
                # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
                self._unique_id = unique_id
            else:
                # Last resort, slow construction of a new array. New memory may be allocated.
                unique_id = _np_.array(unique_id, _np_.uint8).flatten()
                if not unique_id.size == 16:  # Length cannot be checked before casting and flattening
                    raise ValueError(f'unique_id: invalid array length: not {unique_id.size} == 16')
                self._unique_id = unique_id
            assert isinstance(self._unique_id, _np_.ndarray)
            assert self._unique_id.dtype == _np_.uint8  # type: ignore
            assert self._unique_id.ndim == 1
            assert len(self._unique_id) == 16

    @property
    def node_id(self) -> uavcan.node.ID_1_0:
        """
        uavcan.node.ID.1.0 node_id
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._node_id

    @node_id.setter
    def node_id(self, x: uavcan.node.ID_1_0) -> None:
        if isinstance(x, uavcan.node.ID_1_0):
            self._node_id = x
        else:
            raise ValueError(f'node_id: expected uavcan.node.ID_1_0 got {type(x).__name__}')

    @property
    def unique_id(self) -> _NDArray_[_np_.uint8]:
        """
        saturated uint8[16] unique_id
        The setter raises ValueError if the supplied value exceeds the valid range or otherwise inapplicable.
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, x: _NDArray_[_np_.uint8] | list[int] | memoryview | bytes | bytearray ) -> None:
        if isinstance(x, (bytes, bytearray)) and len(x) == 16:
            # Fast zero-copy initialization from buffer. Necessary when dealing with images, point clouds, etc.
            # Mutability will be inherited; e.g., bytes - immutable, bytearray - mutable.
            self._unique_id = _np_.frombuffer(x, _np_.uint8)  # type: ignore
        elif isinstance(x, _np_.ndarray) and x.dtype == _np_.uint8 and x.ndim == 1 and x.size == 16:  # type: ignore
            # Fast binding if the source array has the same type and dimensionality. Beware of the shared reference.
            self._unique_id = x
        else:
            # Last resort, slow construction of a new array. New memory may be allocated.
            x = _np_.array(x, _np_.uint8).flatten()
            if not x.size == 16:  # Length cannot be checked before casting and flattening
                raise ValueError(f'unique_id: invalid array length: not {x.size} == 16')
            self._unique_id = x
        assert isinstance(self._unique_id, _np_.ndarray)
        assert self._unique_id.dtype == _np_.uint8  # type: ignore
        assert self._unique_id.ndim == 1
        assert len(self._unique_id) == 16

    # noinspection PyProtectedMember
    def _serialize_(self, _ser_: _Issue110_) -> None:
        assert _ser_.current_bit_length % 8 == 0, 'Serializer is not aligned'
        _base_offset_ = _ser_.current_bit_length
        _ser_.pad_to_alignment(8)
        self.node_id._serialize_(_ser_)
        assert _ser_.current_bit_length % 8 == 0, 'Nested object alignment error'
        assert len(self.unique_id) == 16, 'self.unique_id: saturated uint8[16]'
        _ser_.add_aligned_array_of_standard_bit_length_primitives(self.unique_id)
        _ser_.pad_to_alignment(8)
        assert 144 <= (_ser_.current_bit_length - _base_offset_) <= 144, \
            'Bad serialization of uavcan.pnp.NodeIDAllocationData.2.0'

    # noinspection PyProtectedMember
    @staticmethod
    def _deserialize_(_des_: _Issue110_) -> NodeIDAllocationData_2_0:
        assert _des_.consumed_bit_length % 8 == 0, 'Deserializer is not aligned'
        _base_offset_ = _des_.consumed_bit_length
        # Temporary _f0_ holds the value of "node_id"
        _des_.pad_to_alignment(8)
        _f0_ = uavcan.node.ID_1_0._deserialize_(_des_)
        assert _des_.consumed_bit_length % 8 == 0, 'Nested object alignment error'
        # Temporary _f1_ holds the value of "unique_id"
        _f1_ = _des_.fetch_aligned_array_of_standard_bit_length_primitives(_np_.uint8, 16)
        assert len(_f1_) == 16, 'saturated uint8[16]'
        self = NodeIDAllocationData_2_0(
            node_id=_f0_,
            unique_id=_f1_)
        _des_.pad_to_alignment(8)
        assert 144 <= (_des_.consumed_bit_length - _base_offset_) <= 144, \
            'Bad deserialization of uavcan.pnp.NodeIDAllocationData.2.0'
        assert isinstance(self, NodeIDAllocationData_2_0)
        return self

    def __repr__(self) -> str:
        _o_0_ = ', '.join([
            'node_id=%s' % self.node_id,
            'unique_id=%s' % _np_.array2string(self.unique_id, separator=',', edgeitems=10, threshold=100, max_line_width=1000000),
        ])
        return f'uavcan.pnp.NodeIDAllocationData.2.0({_o_0_})'

    _FIXED_PORT_ID_ = 8165
    _EXTENT_BYTES_ = 48

    _MODEL_: _pydsdl_.DelimitedType = _restore_constant(
        'ABzY8QiOG40{@*{U#}d+mA|&ZzBJ(QFN7rlnwu=lP3BH8kU;DtyN+#wbz?(}2`EZ3s+q2tF1x3@x2yZk9i&L)VOK;NX|Kerl*fI{'
        'M~GI6qP*p4pYsJ)$~V|N?)g{U)jcy8SOiqhOn23(b55P#@0_Z>A3yLP|Mk`m{j+=_Uqm)a21Bb0qZ0Fx8YOx#9A~pUv!>Lm<)hbi'
        'VrFm|-Cg8*_33K=H>+Q-ddu@elcu^@#XHMK-z$r1Tvml{-}2xvRWs<~g-RWbRXWJid~iF9^v&y6lO!9f(q!p%RjSo;cX*@=3m>t&'
        '3qO<VPgjR$4|o1;^_$i5;h`$a!i=g?+tn|j?=6DYcdeEWzGZY0HPQsb2*w(gC}Mnpzl?+BMG-Cq!3H<4ui{7Ii-%`;*!b~ZuHrAt'
        't<P*5GcQm-<_N}o^8M7BX{w`}X{o2WXzSzQ;mDN3M5og-UL8IL5{;EDhcg&?6~DNA`d!x%J~p@pzum&0Kn*+py1KJkJ~gzZN+VT7'
        'en+2FBbdg6M=Gg6f(M3CHeM}vR@F!?pY*gg94*)!zh1=$@e3BDiF96QFoTX(zg=D&PRy~6hIv+$LldoTFCQP;tSZJDen|8%S1{J{'
        '0yc>mt(FhH3l4JpE`Iwd%<as#VeB|VbDuAvRd%&JH#OyI8C+ZBu}ZG%S+-h!HLpgA84n9Rtr8r$F$z3zo^1g=p*6tjH?I#a4PF_b'
        ')>kE};K^aEEXY#mv_vx;nXz8|HXbbhbX`wOs%@x3eD(mI4DQA{oT+0ot7ajn$3!71DKs{Osp~X?PQok=OSrFsPermY=`<`0m0DCo'
        'n5cy=2EotpDH|r)To-V&O2bR9z8QiHp-SdzVWsm)R=^iY^Sm7dck~3G$!H9l>#>;_c6_>hmO&>bon!;F+$aGZyyTp$F)>WE?0#M?'
        'ANi3fe?p(%gOB25%X7mlUoFFJo!G@}lz{<2lefSi;KC@&JGm}YnHB!(9>)e&PyCbRm)=!T1bSJ!DgG(`db>&zRV=!{LJ#bb|Gw%S'
        'K6YY9u*P%lXmz+-jbOSnlj16X3w4Ya7jPwjS76_VXYje5lf$#pp2POc$>9U?`9b-79@_^_4liJP_T+F^et!tt3nzyGw&za{AIA2<'
        'lfy^k{ztJrcXD`9p8JyY_n18YILm$bgtSje`;@d_miB3Bzas53(*A?A&r17MX}>1zbJ9L9?F-U|(!MC|p0r<=_8ZdvqqHwc`?9n>'
        'Y4@f5rnKLZwlD30v;%3sE$u7PUXu1zX<w7}b!opN?RTYpL)tf`{hqX!rM)8U_oe-Tv_F*gpQQa~Y2TLiLuq4akEQ)Y+TTh0dujh5'
        '?O&w*tF(WU_V3)@+C3u|&$x@8yLi)GyzMSNbQiI^ICdAGxQpMpi{HD8Ke&s(xQoBKi@&*xzsp4hV4#n42pkA}^4-XeD7Ig~h=wsa'
        '9(?%ob2~dXClpR*+FCW$9B(kpKwML4mM&&lWy78s=s_O?k|1qZ=zoDQR_^!VX}A^s#a;jc;Mqb)A%@ITx`v()PVXLqUTSrxf4M{Y'
        'cLTU@br@wD`!2&+9l`hMLL}1ZSocFyhBnTsBy!Tz)3KSxcnuuI8o=N><cEh^=MYdsh%FI@>N3Fl%XwBmBeyaXSc>8xIUtGV2%c)V'
        'ySNX)VF1HZ1!6$_&JugYi9i?;XI8UTK#U@b%?K${KLD)tCzz4y0A;h;3;`!XEKo-oz{M1FD}BNEPOg4fS^P59AQ_0Oj+9A|X9)ZV'
        'f~B_9Dq@IhhMF6OA0$)S7X$56QZK+D3L14%WV4O~IMr1795_Zls6f610CiI6T0Wf4Bm=Yzds#uxPfP)F!Y`jsjjRtfj&-z8{?_S#'
        'Ox8xVjx>+d?<kaJiOPYQFs_2G#_=gL3ZiVD(wxFm=QIG;<ng_)ZsC|kp%%c#-a@{_2z(X4YLmT3hdR+Sq$$iezb@UrbhsP89DghB'
        '18-YC1Pm}&V^b~w0OK3++jLWW7~l3F_K7<{R!XxOsLu}X<D)-~Kj24yj<I9+gd)c;4?m871^*4V0_xcgpq>*zJ-Y=^&kCUK3ZPyP'
        'K;0EUeYgXtyB$D%NC5S$0O~~n)LjA8vjV732%tVHfVwMydQJfK83EL%I)M6!0P3y)>H`9(I|8WB37|eJfcg~y)Tabc9~VHqD1iE~'
        '0P3y)>VpEPX9ZBdDS+A&Kz&I7^&0}HdjhDT0P6Dss9zI6eO3VV83EL%1yG+7Kz*VEs22rL9}z$e1W<PcP|pjXJ|KX4RseP9q>BHD'
        '7aupM@=%o;h-ZQ;-#fdrbC-B9eu;}B>qP27c-IT-?_IrhLxK^8SzgshdSTTa85R0j)sJ;~6FDwLtD1t_YIIMJOAd*&j3GOLwOr!J'
        'V?YuJWDq+b?&`sGKu`cZzD#jp3?zICPtJj)a-hS3NQf#;A-weiMF1eZ@}PnwBb;So?(1ZML*qvaeT^1`K8O{OnGgaoS|F+}=CLNK'
        'PJKdTOCkqmtP|D2#~L|L1<G2vmZRECl@Q3NPZn8C6~=lT)f53lvBp5~G)xh)P0S&D&^BbaLg0z}9E1YAH?Ld%hN5aJ5nLx6E5R91'
        '^(77(w9&hTn-t<nOfoQpO&!02@#;_U)Ayb|v$GTbxr$%?ZT#A;|9K&PJ$|DXzZrioz8qhPzaRe~{^9amo<f$g_vWSVerIDvVDPG+'
        '^~Kj9!~5`mUjycohFKADMg?{wM1#wW!XlYRg`93W0P0IZ2*$_Uj7dg48RxpJRImZeiFG26gU>E<$k>u(fjx1eS3?zKg6ND{Ix*7<'
        '@n)vd3hyQTAjr|ZSHc*u8$h{_5{`9&`bDRM9<1i|#7_n)2Qq=rfl%6@87VWhrl7eZotQb+(`PeJ(Ec*%NRnVjk`59WHVG$MVRZ%<'
        'R-RN-aMS1@hvYV3_a-f%rRP>09(6h*DOJbtswyG5FIgqP6u_Th{wXYE;uu*=dEp1>V!(YyAXOBgdYcZyJYHDrhtup@jl4*DwgN3E'
        'OZSIBu0pbKq)Q&ku}n8L5kE`GAwWqCzWxl+T=%jKK0<cSfVeUHG?<u^IXW`Up%<H>AqU}ml^EAiNMRgh7J$%uEj9Cfd&HRb-c8?i'
        'pV3K1g+2oK2P#C-(M<<u28LHS2hub~7o2<n%+^>`AFX~HwgVZ6TT;I^n~4h)Ix%Ww5*Q`43*e12dxh3Ey45rVst9`EC_IL#Oe!1>'
        '<FBEG7E=}gE|5(o5b4sREJ2PpV!w;@*hEBPGtdD%Nad8qE`#89R?K+$0AWM9oj*aOM<Qyyuv`;2(uQYUoP)NmRs+I~bxt_3*F@ZI'
        '&SLla;O$yjdcammNp_|l#Qt@qCSVs_FVKL>fqz@E4y?^FjIy?l>N$B)UP?ovFiW^XWiEW09N;oY??^2Q3t$F5MI1U<Pul<o(c*gz'
        'WYmwi)X2FON<w6~>3$Gi?K=Go<Zjjp;XsCq2(8)jdy=^6>T(c-;X(LwU1Z+36xvuE3~HaPA6Sh-@)3ReVB16%3Y&?&1w99b3;iJL'
        'hhNOAAb6uf1}xV*sh2Bsr7FE8_IZp*pgh9t4cAtki;+ZT(#cCE<SF4zSph8_at>2uiSF<!curshFbq6y1`~t`lM)>XA=L2nfiqAo'
        '_Mj$4a38PczVIW38R7vXnUMUB!BGLmVY~zjn53AyF{V7*E!Gmsx~WS#s*v3!hN-|>Qi+65k(?34CN4M=k+2#T9z@7wniXKw*{Rxb'
        'j*0pxK~og)@rNYiH3z|+25D4>D*`8K(u(3fEuIZE4=d!g9nbMcQ)t_rI>c}shEi9=z(f@gSFlhGUMV{rRw$6B;Ax#zKV$yP*>L66'
        '&@JXANkGjuftX#wQlQeX&GML{z2XjMc~z3^u#UlJOLUmV{uJ)FJHT7!sAK=qv3VlNim%JIpRDQZ$mlsb!6<|7^f5(Z!dK6Rykxi8'
        '5ksM;Zd3`(F-bnBDS>x;G;j(DgYrWk>e#C<wRqn&$wo|EnDAYC_00q17KXQLLW5fZfB;C<?x#q%l?|GdsK;5rUZ<Nqz#agSMhk!w'
        'BL}%KUl^Pq5~h7hKEaQJxZo4DO`5ThYwIa^2T;ESF7^F(LgwW;HLJz6#`qk+PWftoMW;qs3N|HdA+YjVwN_MVtDH7Rxbi|fFq^VH'
        'c6GREA<tD3V^B~}r!4XuiK16u+XSd-<Zi?K$*~UXQiiNuB<yhlgbPg{!vYF2rqW0d>b2UDp&v@^4zz0^Ojji`Aa}DJLz3Y>pi02T'
        'C9JUoncMZMpdeWb+wT-PJ(vQ6mDU?urqHan9&aPL)gkty5REt-00bg4Ov`O+bl>p;O7Kwa;NdU~NE}sTP0It*3}CvrGB;$VgYbPP'
        'U*OeA@8eQOTw0TEuL}u#5N}i`WC{zH^ir~(JV(uqAZ%!zdT!y;_i<Ku_HGw%aRF>7aZ)xuhj<H|6-mWLDO4KJk5qJzBvXN8N6$U8'
        ')&A58Fl`G;fwzd7)z+1X%MrYKMizT*%;(3priRH8xt7GCu~b-VB1^Zmw8G)BL*VHC4UPjKfa#29(i-(_gZcFu@MNl|7WCHADWP^^'
        'X+|>IHqFuvs)13as)!OH)`TL}Yy``-MLR<cTs2!z)%b(D?DPLMKGV%<k<A?pG6K~*3b0=0CZ|CH?itZHfeZ|u>nYp~#uabn=|ayk'
        'Dt!y>-l%Mszc@WvGlQ%|r5e(gWU=250M5s<Bhcm}NH!4Y7?T``M2<7kh?A;LgvVlb=z7lnAZb&nk4vZIhV4Ud<HF<|xV(fJLx-ws'
        '8V4IFxN}P{{YAvw^HM##2c(a5q^zxw-qz&?hyTq+y8j#sIkTFQC*YuC-KuJFKvxwc?qKXi&{1t|XWC`yu3wvV#|LsRR(HviYNu07'
        '_C%gRaD#Y{7xX<sg}&d}@tK)p>W-<7H%AehmodwJCFF`>>JsN*ZGlO~>=u|5iYUBzo%cgIkkBA_Pj8TWUy6gq2DRAT9F3ht%U(?5'
        'Iz^Q*pjtIS4?7^Z#l1WHvKiP*>1r~8a|p1C7iBrn+si~!*;S}FEJ$!^$?Hhqa)hj!3pS;hLD0izulgf+)w#4)X2wU?a<`tR4iumV'
        'PO%Ta7g|LS9p{P@MpF)m+TJ7!k>$J*(Z}V91hudg4xG4%Hhu@LR?MHshwJUpnbxwiNW^=LA+A8QKXsxM=FEhIhE+p8xB+%>dNE+J'
        'PRTWRpjn2M0irkB^~v$EX13$3W$%`O$>g=+`rQ>*Dtq4{*(^&9`~YJIu9k1H7-SJ9I|bSBX4iIH6U1nT(}m1ftkI1K4N!up%#gt4'
        'QMbIIxy4xZMkjuaIZ7_s8~Q_=oNWsF`<?B}fZ6aE{G`;vIA+=Seh6~~Am+Tl7nZ8^E+jjE)N{l(nz)4HnlZJA32vuAI{Oh8YijRu'
        'Sr0)Nvk|r*-3Gr{ms^Z9<}O&vhCH@#Lio!%!Kefj0zHsot&W1u7CXm#3i7--N_C$L9KOF$veAYFia35u=3->EzDpHsP>9753}6n$'
        'Dd*`MG8MO*j(u^pgX}@ds0XqxJ>ZNBye5#OJ*q1K7Uo6E0Ly9ycXi1qP1$x9_NXq);$e1zH6xxOaojBljimU2k^Lr@b_v)>MuyZV'
        'yq%RU0sL&=>~oozbvPq|MpA4=GLuaL8V;9g7&Sov2qLUiizWO5w_Zx4KW_o#iYv(${=v8?8&_26##I+Mb=J9Q=$#)OClwg07+l3*'
        '72QBdq!v@3r7LFCkJM}%S9z&kQn@n3E@_9R2_(ESN0R7l3kSgY<~m7gR^z*Ao~SWr@15kbQ$yvjhaP5Kv<1aMOrUW@m348JDmYiI'
        '3-mBYCR=r~K#<UPr3Y7{_W6r9i@G9R<)nYVF5Tp*$RDNByLZ*4AqS1FfJo3DEGBwV(DNRxs}Gd0x9TyQbE<kSodO@m-Yrp;Gb*5R'
        'bGMJ#JVu56nJGDm;iNVkDOlC*bX#l2^Sc{o0Gd*eBd6thlHM+gaRuAdq`=$O#Yl#0)KLf;F3#pis~2l5xIXODp|dzwe2A(OcxS`K'
        'sie9g-4n=94;u9e0APqqh~3mxa{s^<Q3hIe;zOSAIIG)1+cmP{i@OFy=Z#5{TmJsZA<-Mv&`+sDqnhw>P7c0EVYWsev6<{S)ES?#'
        'S;AwY*Kxw&NFkr!YE-kuo6rk*P1MOd8KTi#YokNzNS(}wjDu-36#|MH^f%?fIG{Ieu9nn6)zWArkkhz2#hC1%yuVyiB|J}Vb2Z)='
        'p($j=3P}X4PpeD>@wP~)w#syB3J6jQ(AJj}gnYl~Z7jHVyrgUDu3m`Tdv>i-Ks)7;=4R=(s!MJucg-Hu`tj<W%wBBPx%<@c(OL1A'
        '#W_Mh{tZy0xG&ycN6m1NRWD;;s0uu|lHlS}R5PnH2u|}y+S5LYEHnmta#{^e_k>9+D7RzJ74arj_CFiyo#zFgAL`MqPJtt~QnQuD'
        'e2zmJuF86oxHHzqLnt024Wx`Jg*1G5p;+H>zT&%!|HLV~)a+*Moo6shQ1MwFWP$Zzn?_9r^P}v@M6?wT3`E$@RHwRtECqg0YbUri'
        '>dSch7F!C|Yv>2S+Ah`hF{6h35hJrZnX=(vslPn|nxP^Fo?pNbaEGR|<WPk+I7N3nL!1G=FcY>9!-^BwZhWK~3^-Ja8<3wg+b+JF'
        '^u3&ncTvzDtt>0ga(<hoiS29W=sKGl_4%}>OYb!5h7Q+GV)5>bw<^6Ie@!ZFbODMC1Z^e-PS8^!u8p46`m<h95nAm66}=SZoe$_*'
        '$+{ygr@5bmAwF+sH${D^o7XY<t=8^{k0g-GLxeaoD!I((k_t_=E+*8f$)(E8Zql&StzLo*(iI^5BO0wU%T4g17lKlX#1@Y<@jmS~'
        'xW<DwRI+2RpX1pl$`66%?e`(6Zsed85JE38+FrvuU7n1;WA?C+<AKrs75TlXO5!PkQco9M^w-pVnFaM`EUJNzq|Y}NkKB=JUpy%V'
        'Pz92Y-WPHfjSnq2WhfuO1IXTE2s#EUIdX)_9T&qw7v2c0C*_b-;6bp-qTX;#nqGlg=2bE6l+qg#&^<RV8&l4RjvsVfqGQhWbNw1t'
        '1nznn1zM*wTCx`8<Xae5!1@mmn91l~-Q7hAnMljeweI+NjpTmp_rT3DY!rA)5=aM>{8!byAm?70lO)Po;wUM;ieWy&-UC}rAVwJG'
        '8FV^=1;zs?x9-00ck7PvT}zb3iovz3w;MK#c1~~~U*7(#$vV<Z!{-2xF6{>lQ0l%M)qr6_90vRWg4`Gkhsn)`tXobcV^S`WRAJq@'
        'z?V&Ij4ZZ3Mu6w$T+tz*j*(@*aWGnx`hW^$E@Wa{`!T~To@%3Y1<@j#;juY<EhP0)et%WwSg(!3-d*=1j(74+2z5b0ks|pkDAgrc'
        'e6S89pgmU^T{+;^B{kV+8|xzFGa2pIPsrsBE~7$sy)`!wJa}n}z<t@z!m1u^GmkZ|Ie8t2RVc|7*Z;_p6NNmjweuvUr26D4gEQ+%'
        ')-kY@y5Pck3vj;*)zor5!CyI@l3QIxS%*=y%P_W7e1Ne;dYX%{f<}CdiV9*Z3~?%4Db6g7RL#-K1%Y&PEL;qXkLCD2&Di9shIZ5='
        'zTtz60yPdca79*^98!T$d(4ZB#JS!m!*W4_?k7ncIIX|nAVgFsW@jc47HvOJ(&@Z8Q;BC$cyDX0DqEM=@pU3($hoUP5%VEITr3-B'
        'Ny5iF9jN1S!oqcwEJUGo)W;{${X}Se%r#Id%W~FO^H_IwqVLWebvC-2J-9aJ1htJY9Pt7}d66m=d{!Rc@S&~bcI>Y6Pywbv_?}Cw'
        'o6#s4lG(Tk2e@+hOe}EfS)Kt_0f&I7LuZBP6p+(Nqb0#1shN&+3OEdA8dKpWGMz<i(wN<fh&II6`fQ18%oH=65-9wgw5_g}5$GfB'
        'po1P_fMAW6agkNixU*>|?^w{@9o6{mz*Ts45Wa)eL6DB#bwVL8Q<30OmzU!q1_B`KM0Qi>a@wnF58%66Z0b9r?Ym&O!Ug4SU;ycy'
        'sRy-yKOzCauZ-l)5?@<A))KeJk=MoS=NK^TNfgIuw7+FSqasrgzP;adG}npfV=Z}*1hwY(%8FquOHM^Qei0+2`q_p&%CW@yoyOM7'
        '?VDb(#Mfpvyk9wRLpJBacu2QHwEb<M{-y(GpZx}qv*k6iWm|QQzI^cZjXO7Rr-b60mld_%uyOTPmyB<E!NyJRw12MNz7GHIZ8{^@'
        '?7X#?T&<P;E#79!EVo-cr(R%k60A8&A&DNQEe5w=<TwxZ@>;hS-chQLlgWb2-AfqjS`~3#AA~oKaTnX$Pk`L7KCmX`P&uoyu{1F6'
        'p423$Xv+F!cX3(wB5BLo?Id9>0m1DMx1l{)ZGJWKz52?3UGmG<fDb85DK@<^iLYGZUp4^$$G;=8vA1{PUmTvH_a`5Ve+B;yVcb97'
        'hA;kGTm1F}zCCHa{RRF#gSD^uExY*P_>uTA{5vAO`04o1U+68Vd(Xiw_nwFU)h|Kadl5b@FAViD!qDp0$7hyL4<q>lEyXZ~%mSM3'
        '3#VcHa=d?d2LFZ#y>_}$oA<s2UDJnq1Gqwg{Z~rE6PUWM=C9mAu6o+5spp6H`A<8%vhDTMo%mNU1yq@P&D4_aSj{2)`kxzq#fJy~'
        '2b14w3&lnN00'
    )
    assert isinstance(_MODEL_, _pydsdl_.DelimitedType)
