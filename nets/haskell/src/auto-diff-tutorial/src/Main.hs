import Numeric.Backprop
import           Control.Monad.Trans.State
import           Data.Bifunctor
import           Data.Foldable
import           Data.List
import           Data.List.Split
import           Data.Tuple
import           Data.Type.Option
import           GHC.Generics                          (Generic)
import           GHC.TypeNats
import           Lens.Micro hiding                     ((&))
import           Numeric.Backprop
import           Numeric.LinearAlgebra.Static.Backprop
import           Numeric.LinearAlgebra.Static.Vector
import           Numeric.OneLiner
import           System.Random
import qualified Data.Vector.Storable.Sized            as SVS
import qualified Numeric.LinearAlgebra                 as HU
import qualified Numeric.LinearAlgebra.Static          as H
import qualified Prelude.Backprop                      as B

type Model p a b = forall z. Reifies z W
  => Bvar z p
  -> Bvar z a
  -> Bvar z b


