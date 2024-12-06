import os
import re

def clean_filename(filename):
    # 모든 종류의 공백 문자를 제거
    return re.sub(r'\s+', '', filename)

def rename_files():
    # 한글 이름과 영문 이름 매핑
    name_mapping = {
        '서울특별시': 'seoul',
        '부산광역시': 'busan',
        '대구광역시': 'daegu',
        '인천광역시': 'incheon',
        '광주광역시': 'gwangju',
        '대전광역시': 'daejeon',
        '울산광역시': 'ulsan',
        '세종특별자치시': 'sejong',
        '경기도': 'gyeonggi',
        '강원도': 'gangwon',
        '충청북도': 'chungbuk',
        '충청남도': 'chungnam',
        '전라북도': 'jeonbuk',
        '전라남도': 'jeonnam',
        '경상북도': 'gyeongbuk',
        '경상남도': 'gyeongnam',
        '제주특별자치도': 'jeju'
    }

    # media/sido_images 디렉토리 경로
    directory = 'media/sido_images'
    
    # 디렉토리 내의 모든 파일에 대해
    for filename in os.listdir(directory):
        if filename.endswith('.png'):
            # 기본 파일명과 확장자 분리
            name_parts = filename.rsplit('.', 1)
            base_name = name_parts[0]
            
            # 공백 제거
            base_name = clean_filename(base_name)
            
            # '_' 구분자가 있는 경우 처리 (예: '강원도_TGTSB1D.png')
            if '_' in base_name:
                base_name = base_name.split('_')[0]

            # 매핑된 영문 이름이 있는 경우에만 변경
            for kor, eng in name_mapping.items():
                # 한글 이름에서도 공백 제거
                kor_clean = clean_filename(kor)
                if kor_clean in base_name:
                    # 새 파일명 생성
                    new_filename = f"{eng}.png"
                    
                    # 파일 경로 생성
                    old_file = os.path.join(directory, filename)
                    new_file = os.path.join(directory, new_filename)
                    
                    # 이미 같은 이름의 파일이 있는 경우 건너뛰기
                    if os.path.exists(new_file) and old_file != new_file:
                        print(f"Skipping {filename} - {new_filename} already exists")
                        continue
                    
                    # 파일 이름 변경
                    try:
                        os.rename(old_file, new_file)
                        print(f"Renamed {filename} to {new_filename}")
                    except OSError as e:
                        print(f"Error renaming {filename}: {e}")
                    break

if __name__ == "__main__":
    rename_files()
