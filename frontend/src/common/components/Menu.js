import React from 'react'
import { Link } from 'react-router-dom'

export const MemberMenu = () => (<nav>
        <ol>
            <li><Link to='/member-login'>회원가입</Link></li>
            <li><Link to='/member-list'>회원목록</Link></li>
            <li><Link to='/member-register'>회원등록</Link></li>
            <li><Link to='/member-retreive'>회원조회</Link></li>
            <li><Link to='/member-detail'>회원상세</Link></li>
            <li><Link to='/member-modify'>회원수정</Link></li>
            <li><Link to='/member-delete'>회원탈퇴</Link></li>
        </ol>
</nav>

)
export const ItemMenu = () => (<nav>
    <ol>
        <li><Link to='/item-list'>아이템목록</Link></li>
        <li><Link to='/item-register'>아이템등록</Link></li>
        <li><Link to='/item-retreive'>아이템조회</Link></li>
        <li><Link to='/item-detail'>아이템상세</Link></li>
        <li><Link to='/item-modify'>아이템수정</Link></li>
        <li><Link to='/item-delete'>아이템삭제</Link></li>
    </ol>
</nav>

)
export const BoardMenu = () => (<nav>
    <ol>
        <li><Link to='/post-list'>게시글목록</Link></li>
        <li><Link to='/post-register'>게시글쓰기</Link></li>
        <li><Link to='/post-retrieve'>게시글조회</Link></li>
        <li><Link to='/post-detail'>게시글상세</Link></li>
        <li><Link to='/post-modify'>게시글수정</Link></li>
        <li><Link to='/post-delete'>게시글삭제</Link></li>     
    </ol>
</nav>
)

export const StockMenu = () => (<nav>
    <ol>
        <li><Link to='/stock-list'>게시글 목록</Link></li>
        <li><Link to='/stock-write'>게시글 쓰기</Link></li>
        <li><Link to='/stock-read'>게시글 읽기</Link></li>
        <li><Link to='/stock-remove'>회원정보삭제</Link></li>
    </ol>
</nav>
)

