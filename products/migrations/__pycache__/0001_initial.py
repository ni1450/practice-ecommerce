B
    �f�[�  �               @   s2   d dl mZ d dlmZmZ G dd� dej�ZdS )�    )�unicode_literals)�
migrations�modelsc               @   sb   e Zd ZdZg Zejddejddddd�fdej	dd	�fd
e�
� fdejdddd�fgd�gZdS )�	MigrationT�Product�idF�ID)�auto_created�primary_key�	serialize�verbose_name�title�x   )�
max_length�description�price�   g��Q��C@�   )�decimal_places�default�
max_digits)�name�fieldsN)�__name__�
__module__�__qualname__�initial�dependenciesr   �CreateModelr   �	AutoField�	CharField�	TextField�DecimalField�
operations� r$   r$   �4D:\ecommerce\src\products\migrations\0001_initial.pyr      s   
r   N)�
__future__r   �	django.dbr   r   r   r$   r$   r$   r%   �<module>   s   