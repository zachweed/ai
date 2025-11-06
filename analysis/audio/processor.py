import librosa
from matplotlib import plot as plt

class Processor:
  def __init__(path):
    self.file_path = str(path)

  def resample(sr):
    librosa.load(self.file_path, sr = sr)

  def load:
    librosa.load(self.file_path)

  def mfcc_spectogram:
    librosa.feature.melspectogram(y = y, sr = sr, n_mels = 128)

  def log_scale_spectogram:
    librosa.power_to_db(mfcc_spectogram, ref = np.max)

  def display_spectogram:
    y, sr = load
    S = mfcc_spectogram
    librosa.display.specshow(
      log_scale_spectogram, 
      sr = sr, 
      x_axis = 'time',
      y_axis = 'mel'
    )
    plt.title('Mel Spectogram')
    plt.colorbar(format = '%+02.0f dB')
    plt.tight_layout()
    plt.show()